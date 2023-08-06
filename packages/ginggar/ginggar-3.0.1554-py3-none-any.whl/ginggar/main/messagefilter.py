# SPDX-FileCopyrightText: © 2010 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
Message filters. Used for restricting the user's message list by particular criteria.
"""

import abc
import typing as t
import urllib.parse

import django.contrib.auth.models

import ginggar.main.models


class MessageFilter(abc.ABC):
    """
    Base class for a message filter.

    Different instances of different MessageFilter subclasses can be composed together for filter a message source.
    """

    @abc.abstractmethod
    def applyfilter(self, elements: t.Iterable[ginggar.main.models.NewsMessage],
                    user: django.contrib.auth.models.User) -> t.List[ginggar.main.models.NewsMessage]:
        """
        Returns a list of messages that are matched by this filter from the input list.
        """
        pass

    @property
    def native_representation(self):
        """
        Returns a serializable representation for this filter.
        """
        return [type(self).__name__, *self._tonativerepresentation()]

    @abc.abstractmethod
    def _tonativerepresentation(self) -> t.List[t.Any]:
        """
        Returns a serializable representation of the inner data of this filter.
        """
        pass


class AllMessageFilter(MessageFilter):
    """
    Matches all messages.
    """

    def applyfilter(self, elements, user):
        return elements

    def _tonativerepresentation(self):
        return []


class IdMessageFilter(MessageFilter):
    """
    Matches a message with a particular id.
    """

    # noinspection PyShadowingBuiltins
    def __init__(self, id: t.Union[str, int]):
        super().__init__()
        self.id = int(id)

    def applyfilter(self, elements, user):
        return elements.filter(pk=self.id)

    def _tonativerepresentation(self):
        return [self.id]


class TagMessageFilter(MessageFilter):
    """
    Matches messages by tag.
    """

    def __init__(self, tag):
        super().__init__()
        self.tag = tag

    def applyfilter(self, elements, user):
        return elements.filter(tags__in=[ginggar.main.models.Tag.get_tag_by_name(self.tag, user).pk])

    def applyfilternegated(self, elements, user):
        return elements.exclude(tags__in=[ginggar.main.models.Tag.get_tag_by_name(self.tag, user).pk])

    def _tonativerepresentation(self):
        return [self.tag]


class NotMessageFilter(MessageFilter):
    """
    Matches messages by inverting another filter.
    """

    def __init__(self, filterstring):
        super().__init__()
        self.inner = filterbyfilterstring(filterstring)

    def applyfilter(self, elements, user):
        return self.inner.applyfilternegated(elements, user)

    def _tonativerepresentation(self):
        return [self.inner.native_representation]


class CombinationMessageFilter(MessageFilter, abc.ABC):
    """
    Matches messages by a combination of other filters.
    """

    def __init__(self, filterstring):
        super().__init__()
        d = urllib.parse.parse_qs(filterstring)
        i = 0
        self.inner = []
        while str(i) in d:
            self.inner.append(filterbyfilterstring(d[str(i)][0]))
            i += 1

    def _tonativerepresentation(self):
        return [x.native_representation for x in self.inner]


class AndMessageFilter(CombinationMessageFilter):
    """
    Matches messages by an and-combination of other filters.
    """

    def __init__(self, filterstring):
        super().__init__(filterstring)

    def applyfilter(self, elements, user):
        if len(self.inner) > 0:
            r = elements
            for inner in self.inner:
                r = inner.applyfilter(r, user)
            return r
        else:
            return ginggar.main.models.NewsMessage.objects.none()


class OrMessageFilter(CombinationMessageFilter):
    """
    Matches messages by an or-combination of other filters.
    """

    def __init__(self, filterstring):
        super().__init__(filterstring)

    def applyfilter(self, elements, user):
        r = None
        for inner in self.inner:
            rr = inner.applyfilter(elements, user)
            if r:
                r = r | rr
            else:
                r = rr
        return r.distinct()


def filterbyfilterstring(filterstring: str) -> MessageFilter:
    """
    Creates a :py:class:`MessageFilter` for a url-encoded filter string.
    """
    if not filterstring:
        return AllMessageFilter()
    filterdict = urllib.parse.parse_qs(filterstring)
    if "v" in filterdict:
        filtervalue = filterdict["v"][0]
    else:
        filtervalue = ""
    filtertype = filterdict["t"][0]
    if filtertype == "id":
        return IdMessageFilter(filtervalue)
    elif filtertype == "tag":
        return TagMessageFilter(filtervalue)
    elif filtertype == "not":
        return NotMessageFilter(filtervalue)
    elif filtertype == "or":
        return OrMessageFilter(filtervalue)
    elif filtertype == "and":
        return AndMessageFilter(filtervalue)
    else:
        raise Exception(f"unknown filter {filtertype}")
