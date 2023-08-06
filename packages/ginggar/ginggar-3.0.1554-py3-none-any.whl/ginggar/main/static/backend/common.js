/**
* @license
* SPDX-FileCopyrightText: © 2021 Josef Hahn
* SPDX-License-Identifier: AGPL-3.0-only
*/

import {ajax, AjaxError} from '../piweb/comm.js';


class WeakRefDummy { constructor(o) {this.o = o;} deref() {return this.o;} }  // TODO # remove when browsers support it
if (!window.WeakRef)
    window.WeakRef = WeakRefDummy;

/**
* Can be plugged in a Backend for listening to interesting events.
*/
export class BackendListener {

    /**
    * Called when a message was changed (e.g. some meta data, tagging, read flag, ...).
    */
    messageChanged(message) {
    }

    /**
    * Called when a message was removed.
    */
    messageRemoved(msgid) {
    }

    /**
    * Called when a feed was added.
    */
    feedAdded(feedname) {
    }

    /**
    * Called when a config value was changed.
    */
    userConfigurationChanged(key, value) {
    }

}

const ginggarContext = JSON.parse(document.body.getAttribute("data-ginggarcontext"));

/**
* Returns some Ginggar context data values. Those are statically set on page request, embedded in the dom, and do not
* change.
*
* Only used in rare cases (mostly for low-level stuff) where UserConfiguration cannot be used.
*/
export function getGinggarContextValue(key) {
    return ginggarContext[key];
}

/**
* The url subsite, i.e. the path prefix. All absolute url paths must be prefixed by that.
*/
export const subsite = getGinggarContextValue("subsite");

const csrftoken = getGinggarContextValue("csrftoken");

async function ginggar_ajax(cfg) {
    var headers = cfg.headers = cfg.headers || {};
    headers["X-CSRFToken"] = csrftoken;
    cfg.url = subsite + cfg.url;
    return ajax(cfg);
}

/**
* Low-level backend functions.
*
* For some features there are higher-level facilities.
*/
class Backend {

    constructor() {
        this._listeners = [];
        this._tags = {};
    }

    /**
    * Registers a BackendListener.
    */
    registerListener(backendListener) {
        this._listeners.push(new WeakRef(backendListener));
    }

    /**
    * All BackendListener that are registered.
    */
    get listeners() {
        var result = [];
        for (var i=this._listeners.length-1; i>=0; i--) {
            var listener = this._listeners[i].deref();
            if (listener)
                result.push(listener);
            else
                this._listeners.splice(i, 1);
        }
        return result;
    }

    /**
    * Unregisters a BackendListener.
    */
    unregisterListener(backendListener) {
        this._listeners = this.listeners.filter(x => x != backendListener).map(x => new WeakRef(x));
    }

    /**
    * Logout.
    */
    async logout() {
        return ginggar_ajax({
            url: "api/accounts/actions/logout/",
            method: "POST"
        });
    }

    /**
    * Returns all feeds (as list of Feed).
    */
    async listFeeds() {
        var feedsdata = await ginggar_ajax({url: "api/feeds/"});
        var result = [];
        for (let feeddata of feedsdata.list)
            result.push(new Feed(feeddata.pk, feeddata.fields.name, feeddata.fields.url,
                                 feeddata.fields.updateInterval));
        return result;
    }

    /**
    * Adds a new feed.
    */
    async addFeed(name, url, interval) {
        await ginggar_ajax({
            url: "api/feeds/",
            method: "POST",
            data: {name: name, url: url, interval: interval}
        });
        for (let listener of this.listeners)
            listener.feedAdded(name);
    }

    /**
    * Disabled (i.e. removed) a feed.
    */
    async disableFeed(id) {
        return ginggar_ajax({
            url: `api/feeds/${id}/`,
            method: "DELETE"
        });
    }

    /**
    * Crawls the feeds for new messages.
    */
    async crawlFeeds() {
        return ginggar_ajax({
            url: "api/feeds/actions/crawl/",
            method: "POST"
        });
    }

    /**
    * Sets a configuration value.
    */
    async setConfigValue(key, value) {
        await ginggar_ajax({
            url: `api/configs/${key}/`,
            method: "PUT",
            data: {value: value}
        });
        for (let listener of this.listeners)
            listener.userConfigurationChanged(key, value);
    }

    /**
    * Returns a configuration value (or a default value if no such key exists).
    */
    async getConfigValue(key, defaultValue) {
        try {
            return (await ginggar_ajax({url: `api/configs/${key}/`})).value;
        }
        catch (e) {
            if (e.response?.status == 404)
                return defaultValue;
            throw e;
        }
    }

    /**
    * Returns messages (as list of Message).
    *
    * Can be filtered, and can restrict to messages after a particular point in time.
    */
    async listMessages(lasttimestamp, messageFilterString) {
        return Message.messagesDataToMessages(await ginggar_ajax({
            url: "api/messages/",
            data: {lasttimestamp: lasttimestamp, filter: messageFilterString || ""}
        }));
    }

    /**
    * Removes a message.
    */
    async removeMessage(msgid) {
        await ginggar_ajax({
            url: `api/messages/${msgid}/`,
            method: "DELETE"
        });
        for (let listener of this.listeners)
            listener.messageRemoved(msgid);
    }

    /**
    * Sets a tag to a message.
    */
    async tagMessage(msgid, tag) {
        return this._patchMessage(msgid, {tags_add: tag});
    }

    /**
    * Unsets a tag from a message.
    */
    async untagMessage(msgid, tag) {
        return this._patchMessage(msgid, {tags_remove: tag});
    }

    /**
    * Sets the tags for a message to a given list.
    */
    async setTagsForMessage(msgid, tags) {
        return this._patchMessage(msgid, {tags: tagListToTagString(tags)});
    }

    /**
    * Sets or unsets a message as favorite.
    */
    async favoriteMessage(msgid, isFavorite) {
        if (isFavorite)
            return this.tagMessage(msgid, "favorite");
        else
            return this.untagMessage(msgid, "favorite");
    }

    /**
    * Marks a message as seen.
    */
    async markMessageAsSeen(msgid) {
        return this._patchMessage(msgid, {seen: true});
    }

    async _patchMessage(msgid, data) {
        var changedMessages = await Message.messagesDataToMessages(await ginggar_ajax({
            url: `api/messages/${msgid}/`,
            method: "PATCH",
            data: data
        }));
        for (let changedMessage of changedMessages)
            for (let listener of this.listeners)
                listener.messageChanged(changedMessage);
    }

    /**
    * Returns all tags (as list of Tag).
    */
    async listTags() {
        var tagsdata = await ginggar_ajax({url: "api/tags/"});
        var result = [];
        var min = Number.MAX_VALUE;
        var max = -1;
        var avg = 0;
        for (let [id, name, count] of tagsdata.list) {
            if (count > max)
                max = count;
            if (count < min)
                min = count;
            avg += count;
        }
        var m = 2.5 / (max - min);
        for (let [id, name, count] of tagsdata.list)
            result.push(new Tag(id, name, count, 1+(count-min)*m));
        return result;
    }

    /**
    * Returns a Tag by id.
    */
    async getTagById(id) {
        var result = this._tags[id];
        if (!result) {
            if (this._currentListTagsRequest) {
                await this._currentListTagsRequest;
                result = this.getTagById(id);
            }
            else {
                var newtagdict = {};
                var onresolvefcts = [];
                var onrejectfcts = [];
                var currentListTagsRequest = this._currentListTagsRequest = new Promise((resolve, reject) => {
                    onresolvefcts.push(resolve);
                    onrejectfcts.push(reject);
                });
                try {
                    for (let tag of await this.listTags())
                        newtagdict[tag.id] = tag;
                    this._tags = newtagdict;
                }
                catch (e) {
                    this._currentListTagsRequest = undefined;
                    for (let onrejectfct of onrejectfcts)
                        onrejectfct(e);
                    throw e;
                }
                this._currentListTagsRequest = undefined;
                for (let onresolvefct of onresolvefcts)
                    onresolvefct();
                result = newtagdict[id];
            }
        }
        return result;
    }

    /**
    * Removes a tag completely (i.e. from all messages).
    */
    async removeTag(tagname) {
        return ginggar_ajax({
            url: `api/tags/${tagname}/`,
            method: "DELETE"
        });
    }

    /**
    * Returns all filters (as list of FilterInStore).
    */
    async listFilters() {
        var filtersdata = await ginggar_ajax({url: "api/filters"});
        var result = [];
        for (let filterdata of filtersdata.list)
            result.push(new FilterInStore(filterdata[0], filterdata[1]));
        return result;
    }

    /**
    * Stores a filter.
    */
    async storeFilter(filtername, filterstring) {
        return ginggar_ajax({
            url: "api/filters/",
            method: "POST",
            data: {name: filtername, v: filterstring || ""}
        });
    }

    /**
    * Removes a stored filter.
    */
    async removeFilter(filtername) {
        return ginggar_ajax({
            url: `api/filters/${filtername}/`,
            method: "DELETE"
        });
    }

    /**
    * Returns all tag propagation rules (as list of TagPropagationRule).
    */
    async listTagPropagationRules() {
        var rulesdata = await ginggar_ajax({url: "api/tagpropagationrules/"});
        var result = [];
        for (let ruledata of rulesdata.list)
            result.push(new TagPropagationRule(ruledata[0], ruledata[1], ruledata[2]));
        return result;
    }

    /**
    * Adds a new tag propagation rule.
    */
    async addTagPropagationRule(iftags, applyalsotags) {
        return ginggar_ajax({
            url: "api/tagpropagationrules/",
            method: "POST",
            data: {iftags: tagListToTagString(iftags), applyalsotags: tagListToTagString(applyalsotags)}
        });
    }

    /**
    * Removes a tag propagation rule.
    */
    async removeTagPropagationRule(id) {
        return ginggar_ajax({
            url: `api/tagpropagationrules/${id}/`,
            method: "DELETE"
        });
    }

}

/**
* The Backend.
*/
export const backend = new Backend();

/**
* A web feed.
*/
class Feed {

    constructor(id, name, url, updateInterval) {
        this.id = id;
        this.name = name;
        this.url = url;
        this.updateInterval = updateInterval;
    }

}

/**
* A tag.
*/
class Tag {

    constructor(id, name, count, size) {
        this.id = id;
        this.name = name;
        this.count = count;
        this.size = size;
    }

}

/**
* A message.
*/
class Message {

    constructor(id, title, url, summary, createdTime, tags, isFavorite, isUnseen, fetchedAt) {
        this.createdTime = createdTime;
        this.fetchedAt = fetchedAt;
        this.isFavorite = isFavorite;
        this.isUnseen = isUnseen;
        this.id = id;
        this.summary = summary;
        this.tags = tags;
        this.title = title;
        this.url = url;
    }

    /**
    * Generates a list of Message for a raw backend answer.
    */
    static async messagesDataToMessages(messagesdata) {
        var result = [];
        for (let messagedata of messagesdata.list) {
            var messagetags = await Promise.all(
                messagedata.fields.tags.map(async (x) => (await backend.getTagById(x)).name));
            result.push(new Message(messagedata.pk, messagedata.fields.title, messagedata.fields.url,
                                    messagedata.fields.summary, new Date(messagedata.fields.created), messagetags,
                                    messagetags.indexOf("favorite")!=-1, !messagedata.fields.seen,
                                    messagedata.fields.fetchedAt));
        }
        return result;
    }

}

/**
* A stored filter.
*/
export class FilterInStore {

    constructor(name, filterTuple) {
        this.name = name;
        this.filterTuple = filterTuple;
    }

}

/**
* A tag propagation rule.
*/
export class TagPropagationRule {

    constructor(id, iftags, applyalsotags) {
        this.id = id;
        this.iftags = iftags;
        this.applyalsotags = applyalsotags;
    }

}

/**
* Converts a tag string (separated by spaces) to a list of tag names.
*/
export function tagStringToTagList(s) {
    return s.split(" ").filter(x => x.length > 0).sort();
}

/**
* Converts a list of tag names to a tag string (separated by spaces).
*/
export function tagListToTagString(tags) {
    return [...(tags || [])].sort().join(" ");
}
