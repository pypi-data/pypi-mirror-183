# SPDX-FileCopyrightText: © 2010 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
Django views.

Most of them are not actually views for user interface presentation but api implementation.
"""

import subprocess
import time
import urllib.parse

import django.conf
import django.contrib.auth
import django.core.serializers
import django.db
import django.http
import django.shortcuts
import django.views
import django.views.defaults

import ginggar.main.crawler
import ginggar.main.messagefilter
import ginggar.main.models
import ginggar.main.viewutils


class LoginPageView(django.views.View):

    def get(self, request: django.http.HttpRequest) -> django.http.HttpResponse:
        try:
            freshly_initialized = ginggar.main.viewutils.ensure_ginggar_initialized()
        except django.db.OperationalError as e:
            raise RuntimeError("Your database seems to be wrongly configured or not initialized!") from e
        return django.http.HttpResponse(
            ginggar.main.viewutils.render_template(
                "login.html", request=request, templateargs={"nexturl": request.GET.get("next", ""),
                                                             "freshly_initialized": freshly_initialized,
                                                             "was_invalid": bool(request.GET.get("was_invalid"))}))


class IndexPageView(django.views.View):

    @ginggar.main.viewutils.login_required
    def get(self, request: django.http.HttpRequest) -> django.http.HttpResponse:
        hasloggedin = ginggar.main.models.UserConfiguration.get(request.user, "hasloggedin", "0") == "1"
        if not hasloggedin:
            ginggar.main.models.UserConfiguration.set(request.user, "hasloggedin", "1")
        return django.http.HttpResponse(ginggar.main.viewutils.render_template(
            "index.html", request=request, ginggarcontextargs={"firstlogin": not hasloggedin}))


class MessagesView(django.views.View):

    def get(self, request: django.http.HttpRequest) -> django.http.HttpResponse:
        messages = ginggar.main.models.NewsMessage.objects.filter(
            deleted=False, owner=request.user, fetchedAt__gt=int(request.GET.get("lasttimestamp", -1)))
        mfilter = ginggar.main.messagefilter.filterbyfilterstring(request.GET.get("filter", ""))
        messages = mfilter.applyfilter(messages, request.user)
        messages = sorted(messages, key=lambda m: m.created)
        return django.http.JsonResponse({"list": ginggar.main.viewutils.modellist_to_dictlist(messages)})


class MessageView(django.views.View):

    def delete(self, request: django.http.HttpRequest, msgid: int) -> django.http.HttpResponse:
        m = django.shortcuts.get_object_or_404(ginggar.main.models.NewsMessage, pk=msgid, owner=request.user)
        m.delete_later()
        return django.http.JsonResponse({})

    def patch(self, request: django.http.HttpRequest, msgid: int) -> django.http.HttpResponse:
        m = django.shortcuts.get_object_or_404(ginggar.main.models.NewsMessage, pk=msgid, owner=request.user)
        requestargs = ginggar.main.viewutils.request_body_object(request)
        tags = requestargs.get("tags", None)
        tags_add = requestargs.get("tags_add", None)
        tags_remove = requestargs.get("tags_remove", None)
        if not ((tags is None) and (tags_add is None) and (tags_remove is None)):
            if tags is None:
                taglist = [t.name for t in m.tags.all()]
            else:
                taglist = ginggar.main.models.NewsMessage.tagstring_to_taglist(tags)
            for addtag in ginggar.main.models.NewsMessage.tagstring_to_taglist(tags_add or ""):
                taglist.append(addtag)
            for removetag in ginggar.main.models.NewsMessage.tagstring_to_taglist(tags_remove or ""):
                taglist.remove(removetag)
            m.set_tags(taglist)
        seen = requestargs.get("seen", None)
        if seen is not None:
            m.seen = seen
            m.save()
        return django.http.JsonResponse({"list": ginggar.main.viewutils.modellist_to_dictlist([m])})


class TagsView(django.views.View):

    def get(self, request: django.http.HttpRequest) -> django.http.HttpResponse:
        res = []
        for t in ginggar.main.models.Tag.objects.filter(owner=request.user):
            count = len(ginggar.main.models.NewsMessage.objects.filter(tags__pk=t.pk))
            res.append((t.pk, t.name, count))
        res.sort(key=lambda x: x[1])
        res.reverse()
        return django.http.JsonResponse({"list": res})


class TagView(django.views.View):

    def delete(self, request: django.http.HttpRequest, tag: str) -> django.http.HttpResponse:
        t = django.shortcuts.get_object_or_404(ginggar.main.models.Tag, name=tag, owner=request.user)
        t.delete()
        return django.http.JsonResponse({})


class TagPropagationRulesView(django.views.View):

    def get(self, request: django.http.HttpRequest) -> django.http.HttpResponse:
        res = []
        for pr in ginggar.main.models.TagPropagationRule.objects.filter(owner=request.user):
            iftags = [iftag.name for iftag in pr.iftags.all()]
            applyalsotags = [applyalsotag.name for applyalsotag in pr.applyalsotags.all()]
            if len(iftags) == 0 or len(applyalsotags) == 0:
                pr.delete()
            else:
                res.append((pr.pk, iftags, applyalsotags))
        return django.http.JsonResponse({"list": res})

    def post(self, request: django.http.HttpRequest) -> django.http.HttpResponse:
        requestargs = ginggar.main.viewutils.request_body_object(request)
        newiftags = ginggar.main.models.NewsMessage.tagstring_to_taglist(requestargs["iftags"])
        newapplyalsotags = ginggar.main.models.NewsMessage.tagstring_to_taglist(requestargs["applyalsotags"])
        newrule = ginggar.main.models.TagPropagationRule(owner=request.user)
        newrule.save()
        for newiftag in newiftags:
            newrule.iftags.add(ginggar.main.models.Tag.get_tag_by_name(newiftag, request.user))
        for newapplyalsotag in newapplyalsotags:
            newrule.applyalsotags.add(ginggar.main.models.Tag.get_tag_by_name(newapplyalsotag, request.user))
        return django.http.JsonResponse({})


class TagPropagationRuleView(django.views.View):

    def delete(self, request: django.http.HttpRequest, ruleid: int) -> django.http.HttpResponse:
        tpr = django.shortcuts.get_object_or_404(ginggar.main.models.TagPropagationRule, pk=ruleid, owner=request.user)
        tpr.delete()
        return django.http.JsonResponse({})


class FiltersView(django.views.View):

    def get(self, request: django.http.HttpRequest) -> django.http.HttpResponse:
        filters = []
        for k in ginggar.main.models.UserConfiguration.list(request.user):
            if k.startswith("filter:"):
                filters.append((k[7:], ginggar.main.models.UserConfiguration.get(request.user, k)))
        return django.http.JsonResponse({"list": filters})

    def post(self, request: django.http.HttpRequest) -> django.http.HttpResponse:
        requestargs = ginggar.main.viewutils.request_body_object(request)
        ginggar.main.models.UserConfiguration.set(
            request.user, f"filter:{requestargs['name']}",
            ginggar.main.messagefilter.filterbyfilterstring(requestargs["v"]).native_representation)
        return django.http.JsonResponse({})


class FilterView(django.views.View):

    def delete(self, request: django.http.HttpRequest, filtername: str) -> django.http.HttpResponse:
        if not ginggar.main.models.UserConfiguration.remove(request.user, f"filter:{filtername}"):
            raise django.http.Http404()
        return django.http.JsonResponse({})


class FeedsView(django.views.View):

    def get(self, request: django.http.HttpRequest) -> django.http.HttpResponse:
        return django.http.JsonResponse({"list": ginggar.main.viewutils.modellist_to_dictlist(
            ginggar.main.models.Feed.objects.filter(enabled=True, owner=request.user))})

    def post(self, request: django.http.HttpRequest) -> django.http.HttpResponse:
        requestargs = ginggar.main.viewutils.request_body_object(request)
        name = requestargs["name"]
        feedtag = ginggar.main.models.Tag.generate_new_tag_name(name, request.user)
        feed = ginggar.main.models.Feed(url=requestargs["url"], name=name, updateInterval=requestargs["interval"],
                                       owner=request.user)
        feed.save()
        feed.correspondingTags.add(feedtag)
        return django.http.JsonResponse({})


class FeedView(django.views.View):

    def delete(self, request: django.http.HttpRequest, feedid: int) -> django.http.HttpResponse:
        feed = django.shortcuts.get_object_or_404(ginggar.main.models.Feed, pk=feedid, owner=request.user)
        feed.enabled = False
        feed.save()
        return django.http.JsonResponse({})


# noinspection PyUnusedLocal
class FeedsActionCrawlView(django.views.View):

    def post(self, request: django.http.HttpRequest) -> django.http.HttpResponse:
        return django.http.JsonResponse({"report": ginggar.main.crawler.Crawler().crawl()})

    def get(self, request: django.http.HttpRequest) -> django.http.HttpResponse:  # more convenient for curl and friends
        return self.post(request)


class UserConfigurationsView(django.views.View):

    def get(self, request: django.http.HttpRequest) -> django.http.HttpResponse:
        return django.http.JsonResponse({"list": ginggar.main.models.UserConfiguration.list(request.user)})


class UserConfigurationView(django.views.View):

    def get(self, request: django.http.HttpRequest, key: str) -> django.http.HttpResponse:
        value = ginggar.main.models.UserConfiguration.get(request.user, key, defaultvalue=self)
        if value == self:
            raise django.http.Http404()
        return django.http.JsonResponse({"value": value})

    def put(self, request: django.http.HttpRequest, key: str) -> django.http.HttpResponse:
        requestargs = ginggar.main.viewutils.request_body_object(request)
        ginggar.main.models.UserConfiguration.set(request.user, key, requestargs["value"])
        return django.http.JsonResponse({})


class AccountsActionLoginView(django.views.View):

    def post(self, request: django.http.HttpRequest) -> django.http.HttpResponse:
        requestargs = ginggar.main.viewutils.request_body_object(request)
        username = requestargs["username"]
        password = requestargs["password"]
        nexturl = requestargs.get("nexturl", "")
        if not django.conf.settings.EXTERNAL_AUTH_HELPER:
            u = django.contrib.auth.authenticate(username=username, password=password)
        else:
            extp = subprocess.Popen([django.conf.settings.EXTERNAL_AUTH_HELPER, ], stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            username = extp.communicate((username + "\n" + password + "\n").encode())[0].decode().strip()
            u = None
            if len(username) > 0:
                m = django.contrib.auth.models.User.objects.filter(username=username)
                if len(m) == 1:
                    u = django.contrib.auth.authenticate(username=username, password=password)
                    if u is None:
                        m[0].set_password(password)
                        m[0].save()
                        u = django.contrib.auth.authenticate(username=username, password=password)
                elif len(m) == 0:
                    u = django.contrib.auth.models.User.objects.create_user(username, '', password)
                    u.save()
                    u = django.contrib.auth.authenticate(username=username, password=password)
        if u is not None:
            if u.is_active:
                django.contrib.auth.login(request, u)
                return django.shortcuts.redirect(nexturl)
        time.sleep(2)
        gparams = {"next": nexturl, "was_invalid": '1'}
        return django.shortcuts.redirect(f"{django.conf.settings.SUB_SITE}/login/?{urllib.parse.urlencode(gparams)}")


class AccountsActionLogoutView(django.views.View):

    def post(self, request: django.http.HttpRequest) -> django.http.HttpResponse:
        django.contrib.auth.logout(request)
        return django.http.JsonResponse({})
