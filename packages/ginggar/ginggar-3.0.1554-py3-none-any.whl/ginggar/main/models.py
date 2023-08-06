# SPDX-FileCopyrightText: © 2010 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
Models.
"""

import datetime
import json
import typing as t
import unicodedata

from django.db import models
import django.contrib.auth.models

import ginggar.main.userscripting


class Tag(models.Model):
    """
    A tag. To be assigned to a Message.
    """

    name = models.CharField(max_length=255)
    owner = models.ForeignKey(django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE)

    def __str__(self):
        return f"[{self.name};from {self.owner.username}]"

    @staticmethod
    def get_tag_by_name(name: str, owner: django.contrib.auth.models.User) -> "Tag":
        """
        Returns the Tag by name. If it does not yet exist internally, a new one is created.
        """
        fname = Tag.formatted_name(name)
        if not fname:
            return None
        res = Tag.objects.filter(name=fname, owner=owner)
        if len(res) > 0:
            return res[0]
        else:
            newtag = Tag(name=fname, owner=owner)
            newtag.save()
            return newtag

    @staticmethod
    def formatted_name(name: str) -> str:
        """
        Returns a formatted tag name, cleaned up from forbidden characters.
        """
        result = ""
        name = str(name or "")
        for char in name.lower():
            if unicodedata.category(char) in ["Lu", "Ll", "Lt", "LC", "Lo", "N", "Nd", "Nl", "No"]:
                result += char
            elif unicodedata.category(char) in ["P", "Po", "Pf", "Pi", "Pe", "Ps", "Pd", "Pc"]:
                if len(result) > 0 and not result.endswith("-"):
                    result += "-"
        if result.endswith("-"):
            result = result[:-1]
        return result

    @staticmethod
    def generate_new_tag_name(name: str, owner: django.contrib.auth.models.User) -> "Tag":
        """
        Returns a new tag with a name like the given one. If this tag already exists, it will create a new one with a
        similar name!
        """
        res = None
        fname = Tag.formatted_name(name)
        i = 2
        sname = fname
        while (res is None) or (len(res) > 0):
            res = Tag.objects.filter(name=sname, owner=owner)
            if len(res) > 0:
                sname = f"{fname}-{i}"
                i += 1
        return Tag.get_tag_by_name(sname, owner)


class Feed(models.Model):
    """
    A web feed.

    See ginggar.main.crawler for details about how messages are retrieved from feeds.
    """

    url = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE)
    enabled = models.BooleanField(default=True)
    lastFetched = models.DateTimeField(default=datetime.datetime(1954, 6, 7, 13, 37, 00))
    updateInterval = models.IntegerField(default=15)  # in minutes
    correspondingTags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"[{self.name};{self.url};from {self.owner.username}]"


class TagPropagationRule(models.Model):
    """
    A tag propagation rule.

    Those rules are automatically processed in background whenever a tag is assigned to a message, and can lead to
    further tag assignments.

    Whenever a message has all of `iftags`, it also gets all of `applyalsotags` assigned.
    """

    iftags = models.ManyToManyField(Tag, related_name="tif")
    applyalsotags = models.ManyToManyField(Tag, related_name="tapplyalso")
    owner = models.ForeignKey(django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE)

    def __str__(self):
        siftags = ",".join([x.name for x in self.iftags.all()])
        sapplyalsotags = ",".join([x.name for x in self.applyalsotags.all()])
        return f"[tags {siftags} imply {sapplyalsotags};from {self.owner.username}]"


class NewsMessage(models.Model):
    """
    A message from a web feed.
    """

    title = models.CharField(max_length=150)
    summary = models.TextField()
    feed = models.ForeignKey(Feed, on_delete=django.db.models.deletion.CASCADE)
    owner = models.ForeignKey(django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE)
    created = models.DateTimeField(auto_now=False)
    seen = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    url = models.CharField(max_length=400, default="", blank=True)
    guid = models.CharField(max_length=400, default="")
    fetchedAt = models.BigIntegerField(default=0)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"[{self.title}]"

    def __addtag(self, tag: t.Union[str, "Tag"], *, firescript: bool = True) -> "Tag":
        try:
            if tag.owner != self.owner:
                raise Exception("violation detected")
        except AttributeError:
            tag = Tag.get_tag_by_name(tag, self.owner)
        if len(self.tags.filter(pk=tag.pk)) == 0:
            self.tags.add(tag)
            if firescript:
                try:
                    ginggar.main.userscripting.execute_user_script(self.owner, "ontagset", self, tag.name)
                except Exception as e:
                    self.summary += f"<br/><br/>Error in user script: {e}"
                    self.save()
        return tag

    def add_tag(self, tag: t.Union[str, "Tag"]) -> None:
        """
        Adds a tag to this message.
        """
        self.__addtag(tag)
        self.__propagate_tags()

    def remove_tag(self, tag: str) -> None:
        """
        Removes a tag from this message.
        """
        ttag = Tag.objects.filter(owner=self.owner, name=tag)
        if len(ttag) > 0:
            if len(self.tags.filter(pk=ttag[0].pk)) > 0:
                self.tags.remove(ttag[0])

    @staticmethod
    def tagstring_to_taglist(tags: str) -> t.List[str]:
        """
        Returns a list of tag names for a space separated string.
        """
        return [tag for tag in tags.split(" ") if tag]

    def set_tags(self, tags: t.Union[t.List[str], str]) -> None:
        """
        Sets the list of tags for this message.
        """
        if isinstance(tags, str):
            tags = self.tagstring_to_taglist(tags)
        oldtags = list(self.tags.all())
        self.tags.clear()
        for tag in tags:
            ntag = self.__addtag(tag, firescript=False)
            if ntag not in oldtags:
                try:
                    ginggar.main.userscripting.execute_user_script(self.owner, "ontagset", self, ntag.name)
                except Exception as e:
                    self.summary += f"<br/><br/>Error in user script: {e}"
                    self.save()
        self.__propagate_tags()

    def save(self, *args, **kwargs):
        """
        Saves the Django model.

        Also executes some :py:func:`ginggar.main.userscripting.execute_user_script`.
        """
        if self.pk is None:  # fresh message
            try:
                ginggar.main.userscripting.execute_user_script(self.owner, "onnewmessage", self)
            except Exception as e:
                self.summary += f"<br/><br/>Error in user script: {e}"
        return super().save(*args, **kwargs)

    def delete_later(self) -> None:
        """
        Marks a message as deleted.
        """
        self.deleted = True
        self.tags.clear()
        self.save()

    def __propagate_tags(self) -> None:
        done = True
        for rule in TagPropagationRule.objects.filter(owner=self.owner):
            tags = list(self.tags.all())
            match = True
            for iftag in rule.iftags.all():
                if iftag not in tags:
                    match = False
                    break
            if match:
                for applyalsotag in rule.applyalsotags.all():
                    if applyalsotag not in tags:
                        done = False
                        self.add_tag(applyalsotag)
        if not done:
            self.__propagate_tags()


class UserConfiguration(models.Model):
    """
    One user configuration pair of a key and an associated value.

    Can store arbitrary json-serializable objects.

    Usually each pair is owned by a user. However, in a few cases the backend stores global stuff here as well
    (with `user=None`).
    """

    user = models.ForeignKey(django.contrib.auth.models.User, null=True, on_delete=django.db.models.deletion.CASCADE)
    configkey = models.CharField(max_length=200, default="")
    configvalue = models.TextField(default="", blank=True)

    def __str__(self):
        return f"[{self.configkey}={self.configvalue};from {self.user.username if self.user else '(GLOBAL)'}]"

    @staticmethod
    def get(user: django.contrib.auth.models.User, key: str,
            defaultvalue: t.Optional[t.Any] = None) -> t.Optional[t.Any]:
        """
        Returns a user configuration value for a user and key.
        """
        lst = UserConfiguration.objects.filter(user=user, configkey=key)
        if len(lst) == 0:
            return defaultvalue
        else:
            return json.loads(lst[0].configvalue)

    @staticmethod
    def remove(user: django.contrib.auth.models.User, key: str) -> bool:
        """
        Removes a user configuration value for a user and key.
        """
        return UserConfiguration.objects.filter(user=user, configkey=key).delete()[0] > 0

    @staticmethod
    def set(user: django.contrib.auth.models.User, key: str, value: t.Optional[t.Any]) -> None:
        """
        Sets a user configuration value for a user and key.
        """
        lst = UserConfiguration.objects.filter(user=user, configkey=key)
        if len(lst) == 0:
            o = UserConfiguration(user=user, configkey=key)
        else:
            o = lst[0]
        o.configvalue = json.dumps(value)
        o.save()

    @staticmethod
    def list(user: django.contrib.auth.models.User) -> t.List[str]:
        """
        Returns the list of all existing keys for a user.
        """
        return [o.configkey for o in UserConfiguration.objects.filter(user=user)]
