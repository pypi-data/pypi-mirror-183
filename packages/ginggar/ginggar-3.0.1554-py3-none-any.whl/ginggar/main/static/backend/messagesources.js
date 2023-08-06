/**
* @license
* SPDX-FileCopyrightText: © 2021 Josef Hahn
* SPDX-License-Identifier: AGPL-3.0-only
*/

import {backend, BackendListener} from './common.js';


/**
* Base class for a message filter.
*
* Different instances of different MessageFilter subclasses can be composed together for filter a message source.
*/
export class MessageFilter {

    /**
    * Returns a url-encoded string representation for this message filter. Used for communication to the backend.
    */
    toFilterString() {
        throw new Error("Not implemented.");
    }

}

/**
* Matches all messages.
*/
export class AllMessageFilter extends MessageFilter {

    toFilterString() {
        return "";
    }

}

/**
* Matches a message with a particular id.
*/
export class IdMessageFilter extends MessageFilter {

    constructor(id) {
        super();
        this.id = id;
    }

    toFilterString() {
        return `t=id&v=${this.id}`;
    }

}

/**
* Matches messages by tag.
*/
export class TagMessageFilter extends MessageFilter {

    constructor(tag) {
        super();
        this.tag = tag;
    }

    toFilterString() {
        return `t=tag&v=${encodeURIComponent(this.tag)}`;
    }

}

/**
* Matches messages by inverting another filter.
*/
export class NotMessageFilter extends MessageFilter {

    constructor(innerFilter) {
        super();
        this.innerFilter = innerFilter;
        innerFilter.parentFilter = this;
    }

    toFilterString() {
        return `t=not&v=${encodeURIComponent(this.innerFilter.toFilterString())}`;
    }

}

class CombinationMessageFilter extends MessageFilter {

    constructor(operator, innerFilters) {
        super();
        this.operator = operator
        this.innerFilters = innerFilters;
        for (var innerFilter of innerFilters)
            innerFilter.parentFilter = this;
    }

    toFilterString() {
        var res = `t=${this.operator}&v=`;
        for (var i=0; i<this.innerFilters.length; i++) {
            if (i > 0)
                res += encodeURIComponent("&");
            res += encodeURIComponent(i + "=" + encodeURIComponent(this.innerFilters[i].toFilterString()));
        }
        return res;
    }

}

/**
* Matches messages by an and-combination of other filters.
*/
export class AndMessageFilter extends CombinationMessageFilter {

    constructor(innerFilters) {
        super("and", innerFilters);
    }

}

/**
* Matches messages by an or-combination of other filters.
*/
export class OrMessageFilter extends CombinationMessageFilter {

    constructor(innerFilters) {
        super("or", innerFilters);
    }

}

/**
* Can be plugged in a MessageSource for listening to interesting events.
*/
export class MessageSourceListener {

    /**
    * Called when the filter was changed.
    */
    messageFilterChanged(messageSource, messageFilter) {
    }

    /**
    * Called when the list was reset.
    */
    resetList(messageSource) {
    }

    /**
    * Called when a messages arrived.
    */
    messageArrived(messageSource, message) {
    }

    /**
    * Called when a message was changed.
    */
    messageChanged(messageSource, message) {
    }

    /**
    * Called when a message was removed.
    */
    messageRemoved(messageSource, msgid) {
    }

    /**
    * Called at the beginning of asking the backend for new messages.
    */
    beginRequestingMessages(messageSource, isUpdate) {
    }

    /**
    * Called at the end of asking the backend for new messages.
    */
    endRequestingMessages(messageSource) {
    }

}

/**
* A message source. Used for retrieving messages from the backend.
*/
export class MessageSource {

    /**
    * Returns a MessageFilter for a filter tuple.
    */
    static getMessageFilterForFilterTuple(tuple) {
        if (tuple[0] == "AllMessageFilter")
            return new AllMessageFilter();
        else if (tuple[0] == "IdMessageFilter")
            return new IdMessageFilter(tuple[1]);
        else if (tuple[0] == "TagMessageFilter")
            return new TagMessageFilter(tuple[1]);
        else if (tuple[0] == "NotMessageFilter")
            return new NotMessageFilter(MessageSource.getMessageFilterForFilterTuple(tuple[1]));
        else if (tuple[0] == "AndMessageFilter")
            return new AndMessageFilter(tuple.slice(1).map(x => MessageSource.getMessageFilterForFilterTuple(x)));
        else if (tuple[0] == "OrMessageFilter")
            return new OrMessageFilter(tuple.slice(1).map(x => MessageSource.getMessageFilterForFilterTuple(x)));
        else
            throw `unknown filter type ${tuple[0]}`;
    }

    constructor(listener) {
        this._listener = listener;
        this._currentRequestToken = undefined;
        this._backendListener = new MessageSourceBackendListener(this);
        this._reverseSortOrder = false;
        backend.registerListener(this._backendListener);
        setTimeout(this._keepUpToDate.bind(this), 7 * 1000);
    }

    /**
    * The MessageFilter.
    */
    get messageFilter() {
        return this._messagefilter;
    }

    set messageFilter(messagefilter) {
        this._messagefilter = messagefilter;
        this._messagefilterstr = messagefilter?.toFilterString();
        this._lasttimestamp = 0;
        this._listener.messageFilterChanged(this, messagefilter);
        this._listener.resetList(this);
        this.update(true);
    }

    /**
    * If to reverse the sort order.
    */
    get reverseSortOrder() {
        return this._reverseSortOrder;
    }

    set reverseSortOrder(v) {
        this._reverseSortOrder = v;
        if (this.isInitialized)
            this.messageFilter = this.messageFilter;
    }

    /**
    * If this message source ever fetched something (or is in an unused state).
    */
    get isInitialized() {
        return this._lasttimestamp !== undefined;
    }

    async _keepUpToDate() {
        await this.update();
        setTimeout(this._keepUpToDate.bind(this), 30 * 1000);
    }

    /**
    * Asks the backend for an update on messages.
    */
    async update(fake) {
        if (!this.isInitialized)
            return;
        this._listener.beginRequestingMessages(this, !fake);
        var currentRequestToken = this._currentRequestToken = new Object();
        var messages = await backend.listMessages(this._lasttimestamp, this._messagefilterstr);
        if (currentRequestToken != this._currentRequestToken)
            return;
        if (this.reverseSortOrder)
            messages.reverse();
        for (let message of messages) {
            this._listener.messageArrived(this, message);
            this._lasttimestamp = Math.max(this._lasttimestamp, message.fetchedAt);
        }
        this._listener.endRequestingMessages(this);
        backend.crawlFeeds();
    }

}

class MessageSourceBackendListener extends BackendListener {

    constructor(messageSource) {
        super();
        this._messageSource = messageSource;
    }

    messageChanged(message) {
        this._messageSource._listener.messageChanged(this._messageSource, message);
    }

    messageRemoved(msgid) {
        this._messageSource._listener.messageRemoved(this._messageSource, msgid);
    }

    async feedAdded() {
        await backend.crawlFeeds();
        this._messageSource.update();
    }

}
