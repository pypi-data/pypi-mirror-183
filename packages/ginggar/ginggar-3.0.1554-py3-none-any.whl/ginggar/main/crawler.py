# SPDX-FileCopyrightText: © 2010 Josef Hahn
# SPDX-License-Identifier: AGPL-3.0-only

"""
Feed crawlers. Used for polling new messages from the web feeds.
"""

import datetime
import feedparser
import re
import time
import traceback
import typing as t

import django.http
import django.db.transaction

import ginggar.main.models


class Crawler:
    """
    For polling messages, instantiate this class and call crawl().
    """

    def crawl(self) -> str:
        """
        Polls all feeds for new messages and returns a report string (just interesting for diagnostics).
        """
        response = ""
        # lnow is an abstract integer that increases by each fetched message and
        # thereby provides an unique value along all message.
        # will be stored in the messages, so you can sort or filter by it
        lnow = (int(time.time()) - 1000000000) * 1000
        for feed in ginggar.main.models.Feed.objects.all():
            try:
                with django.db.transaction.atomic():
                    if datetime.datetime.now() - feed.lastFetched >= datetime.timedelta(minutes=feed.updateInterval):
                        feed.lastFetched = datetime.datetime.now()
                        feed.save()
                        fetchfeed = True
                    else:
                        fetchfeed = False
            except django.db.DatabaseError:
                fetchfeed = False
            try:
                if fetchfeed:
                    response += f"Processing feed '{feed.name}'...\n"
                    _seen_msgs = []  # we need this for collecting garbage in message storage
                    if feed.enabled:
                        response += "Crawling...\n"
                    else:
                        response += self.__garbage_collector(feed, _seen_msgs)
                        response += "Skipping disabled.\n"
                        continue
                    tempfeed = feedparser.parse(feed.url)
                    for feeditem in tempfeed["items"]:
                        # check if there is a timstamp and its format
                        if "updated_parsed" in feeditem:
                            timestamp = feeditem["updated_parsed"]
                            itemtimestamp = datetime.datetime(*timestamp[:6])
                        elif "published_parsed" in feeditem:
                            timestamp = feeditem["published_parsed"]
                            itemtimestamp = datetime.datetime(*timestamp[:6])
                        elif "date_parsed" in feeditem:
                            timestamp = feeditem["date_parsed"]
                            itemtimestamp = datetime.datetime(*timestamp[:6])
                        else:
                            itemtimestamp = datetime.datetime.now()
                        # get URL
                        itemurl = feeditem["link"]
                        # get title
                        itemtitle = feeditem["title"]
                        resttitle = ''
                        if len(itemtitle) > 140:
                            # look form blank char at position > 140
                            cut = itemtitle.find(" ", 140)
                            if cut == -1:
                                cut = 140
                            temptitle = itemtitle[0:cut] + ' ...'
                            resttitle = '... ' + itemtitle[cut:]
                            itemtitle = temptitle
                        # check if there is a summary
                        if "summary" in feeditem:
                            itemsummary = feeditem["summary"]
                        else:
                            itemsummary = ''
                        # throw away most html stuff
                        itemsummary = self.__cleanhtml(itemsummary, "_blank")
                        if resttitle:
                            itemsummary = resttitle + '\n' + itemsummary
                        # get item id
                        unique = False
                        if "guid" in feeditem:
                            itemguid = feeditem["guid"]
                            unique = True
                        elif "id" in feeditem:
                            itemguid = feeditem["id"]
                        else:
                            itemguid = itemurl
                        _seen_msgs.append(itemguid)
                        # check if this is a double entry
                        filterargs = {"owner": feed.owner} if unique else {"feed": feed}
                        if len(ginggar.main.models.NewsMessage.objects.filter(guid=itemguid, **filterargs)) == 0:
                            # write to db
                            m = ginggar.main.models.NewsMessage(title=itemtitle, summary=itemsummary, feed=feed,
                                                               url=itemurl,
                                                               guid=itemguid, owner=feed.owner, created=itemtimestamp,
                                                               fetchedAt=lnow)
                            lnow += 1
                            m.save()
                            for tag in feed.correspondingTags.all():
                                m.add_tag(tag)
                            m.save()
                            response += f"Adding '{itemguid}'...\n"
                    response += self.__garbage_collector(feed, _seen_msgs)
            except Exception:
                response += traceback.format_exc() + "\n"
        return response

    def __garbage_collector(self, feed: ginggar.main.models.Feed,
                            seen_msgs: t.List[ginggar.main.models.NewsMessage]) -> str:
        res = ""
        for msg in ginggar.main.models.NewsMessage.objects.filter(deleted=True, feed=feed):
            if msg.guid not in seen_msgs:
                res += f"Deleting '{msg.guid}'...\n"
                msg.delete()
        return res

    re_tag = re.compile(r"<[^<>]*>")  # matches to something like <a href="msn.com" /> or <bananatree?>
    re_elementname = re.compile(r"[^A-Za-z]*([A-Za-z]*)[^A-Za-z]")  # matches to the 'a' in <a href="msn.com" />
    re_attribute = re.compile(r"[^A-Za-z]([A-Za-z]*)\s*"
                              r"=\s*(('[^']*')|(\"[^\"]*\"))")  # matches to 'href="msn.com"' in <a href="msn.com" />
    re_slashatbegin = re.compile(r"<\s*/")
    re_slashatend = re.compile(r"/\s*>")

    def __translatetag(self, s: str, linktarget: str, tree: t.List) -> str:
        elementname = self.re_elementname.search(s).group(1).lower()
        attributes = {}
        for match in self.re_attribute.finditer(s):
            name = match.group(1)
            value = match.group(2)[1:-1]
            attributes[name] = value
        isslashatbegin = self.re_slashatbegin.search(s) is not None
        isslashatend = self.re_slashatend.search(s) is not None
        if elementname == "a":
            if isslashatend:
                return ""
            if isslashatbegin:
                if "a" in tree:
                    tree.pop()
                    return "</a>"
            if "href" not in attributes:
                return ""
            if "a" in tree:
                return ""
            tree.append("a")
            return "<a onclick=\"return true;\" href=\"" + attributes["href"] + "\" target=\"" + linktarget + "\">"
        elif elementname == "img":
            if "src" in attributes:
                if "a" in tree:
                    if "alt" in attributes:
                        return " [Image: " + attributes["alt"] + "] "
                    else:
                        return " [Image: " + attributes["src"] + "] "
                else:
                    alttxt = attributes["src"]
                    if "alt" in attributes:
                        alttxt = attributes["alt"]
                    return " <a onclick=\"return true;\" href=\"" + attributes[
                        "src"] + "\" target=\"" + linktarget + "\">[Image: " + alttxt + "]</a> "
            else:
                return ""
        elif elementname == "br":
            return "<br/>"
        elif elementname == "p":
            return "<br/>"
        else:
            return ""

    def __cleanhtml(self, s: str, linktarget: str) -> str:
        result = ""
        cursor = 0
        tree = []
        for match in self.re_tag.finditer(s):
            startidx = match.start()
            endidx = match.end()
            result = result + s[cursor:startidx] + self.__translatetag(s[startidx:endidx], linktarget, tree)
            cursor = endidx
        result = result + s[cursor:]
        return result
