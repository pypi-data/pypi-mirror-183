/**
* @license
* SPDX-FileCopyrightText: © 2021 Josef Hahn
* SPDX-License-Identifier: AGPL-3.0-only
*/

import {tagListToTagString, tagStringToTagList} from '../backend/common.js';
import {animateCollapseNode, animateExpandNode} from '../pageresources/base.js';
import {animateNode} from '../piweb/animation.js';
import {messageDialog} from '../piweb/conversationdialog.js';
import {baseStylesRef} from '../piweb/styling.js';


const listTemplate = document.createElement("template");
listTemplate.innerHTML = `
    ${baseStylesRef()}
    <style>
        :focus {
            outline: none;
        }
        .selected {
            color: black;
        }
        #outer {
            position: relative;
        }
        #list {
            color: #777777;
            cursor: pointer;
            border-color: #bd8f54;
            border-style: solid;
            border-width: 0 var(--sl-spacing-xxx-small) 0 var(--sl-spacing-xxx-small);
        }
        #selectionframe {
            position: absolute;
            left: var(--sl-spacing-xx-small);
            right: var(--sl-spacing-xx-small);
            transition: top var(--sl-transition-slow), height var(--sl-transition-slow),
                        opacity var(--sl-transition-slow);
            pointer-events: none;
            box-sizing: border-box;
            opacity: 0;
        }
        #selectionframe.visible {
            opacity: 1;
        }
        #selectionframe-border {
            position: absolute;
            top: 0.2rem;
            left: 0.1rem;
            bottom: 0.2rem;
            right: 0.1rem;
            border: 0.2rem dashed #db9c07;
            border-radius: 1rem;
            pointer-events: none;
        }
        #lblnomessages,
        #spinner {
            position: absolute;
            top: 0;
        }
        #lblnomessages {
            color: #f4d69c;
            margin: var(--sl-spacing-xx-large);
        }
        #spinner {
            margin: 10rem 50% 0 50%;
            font-size: 3rem;
        }
    </style>
    <div id="outer">
        <div id="list"></div>
        <div id="selectionframe">
            <div id="selectionframe-border"></div>
        </div>
        <div id="lblnomessages"></div>
        <sl-spinner id="spinner"></sl-spinner>
    </div>
`;

/**
* A message list.
*/
export class MessageList extends HTMLElement {

    constructor() {
        super();
        this.tabIndex = 0;
        this._shadow = this.attachShadow({ mode: "open" });
        this._shadow.appendChild(listTemplate.content.cloneNode(true));
        this._list = this._shadow.getElementById("list");
        this._selectionframe = this._shadow.getElementById("selectionframe");
        this._lblnomessages = this._shadow.getElementById("lblnomessages");
        this._spinner = this._shadow.getElementById("spinner");
        this._list.tabIndex = 0; //TODO see some lines above >> this.tabIndex = 0;
        this.addEventListener("keydown", this._handleKeyDown.bind(this))
        this._scrolldelta = 0;
        this._scrolldestmessageui = undefined;
        this.reset();
        var ro = new ResizeObserver(this._positionSelectionFrame.bind(this));
        ro.observe(this._selectionframe);
    }

    /**
    * Resets the list (i.e. removes all elements from it).
    */
    reset() {
        this._list.innerHTML = "";
        this._selectMessage(undefined);
        this._selectedMessageIsExpanded = false;
        this._handleViewState();
    }

    /**
    * Changes a message.
    */
    changeMessage(message) {
        for (let messageui of this._list.childNodes) {
            if (messageui.msgid == message.id) {
                this._applyMessageToMessageUi(message, messageui);
                break;
            }
        }
    }

    /**
    * Removes a message.
    */
    async removeMessage(msgid) {
        for (let messageui of this._list.childNodes) {
            if (messageui.msgid == msgid) {
                if (messageui == this._selectedMessage) {
                    this._navigateSelectionBy(+1);
                    if (messageui == this._selectedMessage) {
                        this._navigateSelectionBy(-1);
                        if (messageui == this._selectedMessage)
                            this._selectMessage(undefined);
                    }
                }
                messageui._removed = true;
                await animateCollapseNode(messageui);
                messageui.parentNode.removeChild(messageui);
                break;
            }
        }
        this._handleViewState();
    }

    /**
    * Adds a message.
    */
    addMessage(message) {
        var self = this;
        let messageui = document.createElement("ginggar-messagelistentry");
        this._list.appendChild(messageui);
        animateExpandNode(messageui);
        messageui.msgid = message.id;
        this._applyMessageToMessageUi(message, messageui);
        messageui.addEventListener("activate", () => {
            if (self._selectedMessage !== messageui) {
                self._selectMessage(messageui);
                self._expandMessage(true);
            }
            else
                self._expandMessage(!self._selectedMessageIsExpanded);
        });
        messageui.addEventListener("command", async (event) => {
            function scrollupdown(direction) {
                var lastmessageui = self._selectedMessage;
                var newselection = self._getMessageByOffset(direction);
                if (direction > 0)
                    self._selectMessage(newselection);
                if (lastmessageui)
                    self._scrollMessageToPosition(lastmessageui, newselection);
                if (direction < 0)
                    self._selectMessage(newselection);
            }
            if (event.detail.name == "up")
                scrollupdown(-1);
            else if (event.detail.name == "down")
                scrollupdown(+1);
            else if (event.detail.name == "collapse")
                self._expandMessage(false);
            else if (event.detail.name == "remove") {
                if (messageui.isFavorite) {
                    await messageDialog({
                        message: "This is one of your favorites!\n\nIf you really want to delete it,"
                                 + " you have to relieve it from that before."
                    });
                    return;
                }
                self.dispatchEvent(new CustomEvent("remove", {
                    detail: {msgid: message.id},
                    bubbles: true
                }));
            }
            else if (event.detail.name == "favorite")
                self.dispatchEvent(new CustomEvent("favorite", {
                    detail: {msgid: message.id, isFavorite: !messageui.isFavorite},
                    bubbles: true
                }));
            else if (event.detail.name == "tags")
                self.dispatchEvent(new CustomEvent("tags", {
                    detail: {msgid: message.id, msgtitle: messageui.title, msgtags: messageui.tags},
                    bubbles: true
                }));
        });
        messageui.addEventListener("tagselected", (event) => {
            self.dispatchEvent(new CustomEvent("tagselected", {detail: {name: event.detail.name}, bubbles: true}));
        });
        this._handleViewState();
    }

    /**
    * The id of the currently selected message.
    */
    get selectedMessageId() {
        return parseInt(this._selectedMessage?.msgid);
    }

    static get observedAttributes() {
        return ["is-loading", "no-messages-info"];
    }

    /**
    * If to show a loading indicator.
    */
    get isLoading() {
        return this.hasAttribute("is-loading");
    }

    set isLoading(v) {
        if (v)
            this.setAttribute("is-loading", v);
        else
            this.removeAttribute("is-loading");
    }

    /**
    * Which info text to show for an empty list.
    */
    get noMessagesInfo() {
        return this.getAttribute("no-messages-info");
    }

    set noMessagesInfo(v) {
        this.setAttribute("no-messages-info", v);
    }

    attributeChangedCallback(name, oldVal, newVal) {
        if (name == "no-messages-info")
            this._lblnomessages.textContent = newVal;
        else if (name == "is-loading")
            this._handleViewState();
    }

    async _handleViewState() {
        const NORMAL = 0;
        const LOADING = 1;
        const NOMESSAGES = 2;
        var tgtviewstate = NORMAL;
        if (this.isLoading)
            tgtviewstate = LOADING;
        else if (this._messageNodes().length == 0)
            tgtviewstate = NOMESSAGES;
        if (this._viewstate !== tgtviewstate) {
            this._viewstate = tgtviewstate;
            ((tgtviewstate == LOADING) ? animateExpandNode : animateCollapseNode)(this._spinner);
            ((tgtviewstate == NOMESSAGES) ? animateExpandNode : animateCollapseNode)(this._lblnomessages);
        }
    }

    _applyMessageToMessageUi(message, messageui) {
        function convert(value, prop) {
            if (prop == "createdTime")
                return value.toLocaleString();
            else if (prop == "tags")
                return tagListToTagString(value);
            else
                return value;
        }
        for (let prop in message)
            messageui[prop] = convert(message[prop], prop);
    }

    _scrollMessageToPosition(srcmessageui, destmessageui) {
        var alreadyrunning = Boolean(this._scrolldestmessageui);
        this._scrolldestmessageui = destmessageui;
        this._scrolllastdiff = Number.MAX_VALUE;
        if (!alreadyrunning) {
            this._srcmessagetop = Math.floor(srcmessageui.getBoundingClientRect().top);
            setTimeout(this._scrollMessageToPosition_helper.bind(this));
        }
    }

    _scrollMessageToPosition_helper() {
        var self = this;
        var diff = this._scrolldestmessageui.getBoundingClientRect().top - this._srcmessagetop;
        var absdiff = Math.abs(diff);
        if (this._scrolllastdiff > absdiff) {
            this._scrolllastdiff = absdiff;
            var step = (absdiff > 1) ? (Math.sign(diff) * Math.min(5, Math.ceil(absdiff / 3))) : diff;
            if (this._list.children.length > 0) {
                var currentscrollpos = -this._list.children[0].getBoundingClientRect().top;
                var scrolldummy = document.createElement("div");
                scrolldummy.style.position = "absolute";
                scrolldummy.style.top = `${currentscrollpos+step}px`;
                this._list.appendChild(scrolldummy);
                scrolldummy.scrollIntoView();
                this._list.removeChild(scrolldummy);
                if (absdiff > 1) {
                    setTimeout(() => { self._scrollMessageToPosition_helper() }, 60);
                    return;
                }
            }
        }
        this._scrolldestmessageui = undefined;
    }

    _handleKeyDown(event) {
        if (event.altKey || event.ctrlKey || event.metaKey)
            return;
        if (event.key == "ArrowUp") {
            this._scrollByElement(-1);
            event.preventDefault();
        }
        else if (event.key == "ArrowDown") {
            this._scrollByElement(+1);
            event.preventDefault();
        }
        else if (event.key == "ArrowRight") {
            if (this._selectedMessage) {
                window.open(this._selectedMessage.url, "_blank", "noopener");
                this._markMessageSeen(this._selectedMessage);
            }
            event.preventDefault();
        }
        else if (event.key == "Delete") {
            if (this._selectedMessage)
                this._selectedMessage.dispatchEvent(
                    new CustomEvent("command", {detail: {name: "remove"}, bubbles: true}));
            event.preventDefault();
        }
        else if (event.key == "+") {
            this._expandMessage(!this._selectedMessageIsExpanded);
            event.preventDefault();
        }
        else if (event.key == "-") {
            this._expandMessage(false);
            event.preventDefault();
        }
        else if (event.key == "f") {
            if (this._selectedMessage)
                this._selectedMessage.dispatchEvent(
                    new CustomEvent("command", {detail: {name: "favorite"}, bubbles: true}));
            event.preventDefault();
        }
        else if (event.key == "t") {
            if (this._selectedMessage)
                this._selectedMessage.dispatchEvent(
                    new CustomEvent("command", {detail: {name: "tags"}, bubbles: true}));
            event.preventDefault();
        }
        else if (event.key == "PageUp") {
            this._scrollByPage(-1);
            event.preventDefault();
        }
        else if (event.key == "PageDown") {
            this._scrollByPage(+1);
            event.preventDefault();
        }
    }

    _scrollByPage(direction) {
        var tgtmessageui;
        var innerheight = window.innerHeight;
        for (let messageui of this._messageNodes()) {
            var rect = messageui.getBoundingClientRect();
            if (direction < 0 && rect.bottom > 0) {
                tgtmessageui = messageui;
                break;
            }
            else if (direction > 0 && rect.top < innerheight)
                tgtmessageui = messageui;
        }
        if (tgtmessageui) {
            if (tgtmessageui == this._selectedMessage)
                this._scrollByElement(direction);
            else {
                this._selectMessage(tgtmessageui);
                this._scrollAlignedToSelection(direction);
            }
        }
    }

    _scrollAlignedToSelection(direction) {
        if (!this._selectedMessage)
            return;
        var keyscrolltoken = this._currentkeyscrolltoken = new Object();
        function _exec(count) {
            if (keyscrolltoken != this._currentkeyscrolltoken)
                return;
            var currrect = this._selectedMessage.getBoundingClientRect();
            if ((direction > 0) ? (currrect.bottom > window.innerHeight) : (currrect.top < 0))
                this._getMessageByOffset((direction > 0) ? -2 : 0).scrollIntoView(
                        {block: (direction > 0) ? "start" : "end", behavior: "smooth"});
            if (count)
                setTimeout(_exec.bind(this), 600, count-1);
        }
        setTimeout(_exec.bind(this), 400, 1);
    }

    _scrollByElement(direction) {
        this._navigateSelectionBy(direction);
        this._scrollAlignedToSelection(direction);
    }

    _messageNodes() {
        return [...this._list.children].filter(x => !x._removed);
    }

    _markMessageSeen(messageui) {
        messageui.isUnseen = false;
        this.dispatchEvent(new CustomEvent("seen", {detail: {msgid: messageui.msgid}, bubbles: true}));
    }

    _getMessageByOffset(offset) {
        var msgnodes = this._messageNodes();
        var oldindex = this._selectedMessage ? msgnodes.indexOf(this._selectedMessage) : -1;
        var newindex = Math.min(Math.max(0, oldindex + offset), msgnodes.length - 1);
        return msgnodes[newindex];
    }

    _navigateSelectionBy(offset) {
        this._selectMessage(this._getMessageByOffset(offset));
    }

    _expandMessage(expand) {
        if (!this._selectedMessage)
            return;
        if (Boolean(this._selectedMessageIsExpanded) != Boolean(expand)) {
            if (expand) {
                this._selectedMessage.expand();
                this._markMessageSeen(this._selectedMessage);
            }
            else
                this._selectedMessage.collapse();
            this._selectedMessageIsExpanded = expand;
        }
        this._positionSelectionFrame();
    }

    _selectMessage(messageui) {
        if (this._selectedMessage == messageui)
            return;
        var expanded = this._selectedMessageIsExpanded;
        this._expandMessage(false);
        if (this._selectedMessage)
            this._selectedMessage.classList.remove("selected");
        this._selectedMessage = messageui;
        if (messageui) {
            messageui.classList.add("selected");
            this._selectionframe.classList.add("visible");
        }
        else
            this._selectionframe.classList.remove("visible");
        this._expandMessage(expanded);
        this._positionSelectionFrame();
    }

    _positionSelectionFrame(count) {
        var self = this;
        if (count === undefined)
            count = 3;
        if (count)
            setTimeout(() => {
                self._positionSelectionFrame_once();
                self._positionSelectionFrame(count-1);
            }, 200);
    }

    _positionSelectionFrame_once() {
        var top = 0;
        var height = 0;
        if (this._selectedMessage) {
            top = this._selectedMessage.offsetTop;
            height = this._selectedMessage.getBoundingClientRect().height;
        }
        this._selectionframe.style.top = `${top}px`;
        this._selectionframe.style.height = `${height}px`;
    }

}

customElements.define("ginggar-messagelist", MessageList);


const entryTemplate = document.createElement("template");
entryTemplate.innerHTML = `
    ${baseStylesRef()}
    <style>
        :host {
            display: block;
            --panel-background: #ffffffe4;
        }
        #frame {
            padding: 0 var(--sl-spacing-medium);
            border-bottom: 0.0625em solid #999999;
            background: #ffffff;
        }
        #title {
            padding: var(--sl-spacing-x-small) 0;
            font-size: 1.2em;
            transition: color var(--sl-transition-slow), text-shadow var(--sl-transition-slow);
        }
        .unseen #title {
            color: #000000;
        }
        .favorite #title {
            color: #2d1300;
            text-shadow: 0.17em 0.17em 0.25em #dd5a0c;
        }
        #summary {
            margin: var(--sl-spacing-medium);
            cursor: initial;
        }
        .actions {
            margin-top: var(--sl-spacing-small);
        }
        .actions sl-button {
            margin-right: var(--sl-spacing-xx-small);
        }
        .detaillabel {
            font-size: 0.8em;
            color: #444444;
        }
        #tags {
            margin: 0.25em 0 0.8em 0;
        }
        #tags::part(base) {
            flex-wrap: wrap;
        }
        #tags ginggar-tagbutton {
            margin: var(--sl-spacing-xx-small) var(--sl-spacing-xx-small) 0 0;
        }
        #topstickypart {
            position: sticky;
            top: var(--topstickypart-distance, 0);
        }
        .topshadowpart {
            box-shadow: 0 0.4em 0.67em var(--panel-background);
        }
        #bottomstickypart {
            position: sticky;
            bottom: var(--bottomstickypart-distance, 0);
            box-shadow: 0 -0.4em 0.67em var(--panel-background);
        }
        #topstickypart,
        #bottomstickypart {
            background: var(--panel-background);
        }
        @keyframes ginggar-collapse {
            100% {
                opacity: 0;
                max-height: 0;
                margin: 0;
            }
        }
        @keyframes ginggar-expand {
            100% {
                opacity: 1;
                max-height: 100rem;
            }
        }
    </style>
    <div id="frame">
        <div id="topstickypart">
            <div id="title"></div>
            <div class="hides-on-collapse topshadowpart">
                <sl-button-group class="actions">
                    <sl-button id="btnup" title="Keyboard: arrow up">
                        <sl-icon name="chevron-up"></sl-icon>
                    </sl-button>
                    <sl-button id="btncollapse" title="Keyboard: + and -">
                        <sl-icon name="arrows-collapse"></sl-icon>
                    </sl-button>
                    <sl-button id="btndown" title="Keyboard: arrow down">
                        <sl-icon name="chevron-down"></sl-icon>
                    </sl-button>
                </sl-button-group>
                <sl-button-group class="actions">
                    <sl-button id="btnremove" title="Keyboard: del">
                        <sl-icon name="trash"></sl-icon> Remove
                    </sl-button>
                    <sl-button id="btnfavorite" title="Keyboard: f">
                        <sl-icon name="star" id="btnfavorite-icon"></sl-icon> Favorite
                    </sl-button>
                    <sl-button id="btntags" title="Keyboard: t">
                        <sl-icon name="tags"></sl-icon> Tags
                    </sl-button>
                    <sl-button id="btnvisit" title="Keyboard: arrow right">
                        <sl-icon name="box-arrow-up-right"></sl-icon> Visit
                    </sl-button>
                </sl-button-group>
                <div class="detaillabel">
                    <span id="createdtime"></span>
                </div>
            </div>
        </div>
        <div id="summary" class="hides-on-collapse">
        </div>
        <div id="bottomstickypart" class="hides-on-collapse">
            <sl-button-group id="tags">
            </sl-button-group>
        </div>
    </div>
`;

/**
* One entry in a MessageList.
*/
export class MessageListEntry extends HTMLElement {

    constructor() {
        super();
        var self = this;
        this._shadow = this.attachShadow({ mode: "open" });
        this._shadow.appendChild(entryTemplate.content.cloneNode(true));
        this._titlediv = this._shadow.getElementById("title");
        this._framediv = this._shadow.getElementById("frame");
        this._titlediv.addEventListener("click", ()=>{
            self.dispatchEvent(new Event("activate"));
        });
        this._btnvisit = this._shadow.getElementById("btnvisit");
        this._btnvisit.target = "_blank";
        this._btnvisit.rel = "noopener";
        this._imgfavorite = this._shadow.getElementById("btnfavorite-icon");
        this._lblcreatedtime = this._shadow.getElementById("createdtime");
        this._lblsummary = this._shadow.getElementById("summary");
        this._pnltags = this._shadow.getElementById("tags");
        var btnup = this._shadow.getElementById("btnup");
        var btncollapse = this._shadow.getElementById("btncollapse");
        var btndown = this._shadow.getElementById("btndown");
        var btnremove = this._shadow.getElementById("btnremove");
        var btnfavorite = this._shadow.getElementById("btnfavorite");
        var btntags = this._shadow.getElementById("btntags");
        for (let [btn, cmdname] of [[btnup, "up"], [btncollapse, "collapse"], [btndown, "down"],
                    [btnremove, "remove"], [btnfavorite, "favorite"], [btntags, "tags"]])
            btn.addEventListener("click", () => {
                self.dispatchEvent(new CustomEvent("command", {detail: {name: cmdname}, bubbles: true}));
            });
        this._collapsingParts = this._framediv.querySelectorAll(".hides-on-collapse");
        this.collapse("0s");
    }

    static get observedAttributes() {
        return ["created-time", "is-favorite", "is-unseen", "msgid", "summary", "tags", "title", "url"];
    }

    /**
    * The message creation time.
    */
    get createdTime() {
        return this.getAttribute("created-time");
    }

    set createdTime(v) {
        this.setAttribute("created-time", v);
    }

    /**
    * If this message is marked as favorite.
    */
    get isFavorite() {
        return this.hasAttribute("is-favorite");
    }

    set isFavorite(v) {
        if (v)
            this.setAttribute("is-favorite", v);
        else
            this.removeAttribute("is-favorite");
    }

    /**
    * If the message was not yet seen by the owner.
    */
    get isUnseen() {
        return this.hasAttribute("is-unseen");
    }

    set isUnseen(v) {
        if (v)
            this.setAttribute("is-unseen", v);
        else
            this.removeAttribute("is-unseen");
    }

    /**
    * The message id.
    */
    get msgid() {
        return this.getAttribute("msgid");
    }

    set msgid(v) {
        this.setAttribute("msgid", v);
    }

    /**
    * The message summary.
    */
    get summary() {
        return this.getAttribute("summary");
    }

    set summary(v) {
        this.setAttribute("summary", v);
    }

    /**
    * The message tags (as space separated string).
    */
    get tags() {
        return this.getAttribute("tags");
    }

    set tags(v) {
        this.setAttribute("tags", v);
    }

    /**
    * The message title.
    */
    get title() {
        return this.getAttribute("title");
    }

    set title(v) {
        this.setAttribute("title", v);
    }

    /**
    * The message url.
    */
    get url() {
        return this.getAttribute("url");
    }

    set url(v) {
        this.setAttribute("url", v);
    }

    /**
    * Expands this node.
    */
    expand(animationTime) {
        animationTime = animationTime || getComputedStyle(this).getPropertyValue("--sl-transition-x-slow");
        for (let node of this._collapsingParts) {
            node.style.maxHeight = `${node.getBoundingClientRect().height}px`;
            node.style.display = "";
            (async () => {
                if (await animateNode(node, "ginggar-expand", animationTime))
                    node.style.maxHeight = "";
            })();
        }
    }

    /**
    * Collapse this node.
    */
    collapse(animationTime) {
        animationTime = animationTime || getComputedStyle(this).getPropertyValue("--sl-transition-slow");
        for (let node of this._collapsingParts) {
            node.style.maxHeight = `${node.getBoundingClientRect().height}px`;
            (async () => {
                if (await animateNode(node, "ginggar-collapse", animationTime))
                    node.style.display = "none";
            })();
        }
    }

    attributeChangedCallback(name, oldVal, newVal) {
        var self = this;
        if (name == "created-time")
            this._lblcreatedtime.textContent = newVal;
        else if (name == "is-favorite") {
            if (newVal !== null)
                this._framediv.classList.add("favorite");
            else
                this._framediv.classList.remove("favorite");
            this._imgfavorite.name = (newVal !== null) ? "star-fill" : "star";
        }
        else if (name == "is-unseen") {
            if (newVal !== null)
                this._framediv.classList.add("unseen");
            else
                this._framediv.classList.remove("unseen");
        }
        else if (name == "summary")
            this._lblsummary.innerHTML = newVal;
        else if (name == "tags") {
            this._pnltags.innerHTML = "";
            for (let tag of tagStringToTagList(newVal)) {
                let btntag = document.createElement("ginggar-tagbutton");
                btntag.textContent = tag;
                btntag.title = `tag: ${tag}`;
                btntag.addEventListener("click", () => {
                    self.dispatchEvent(new CustomEvent("tagselected", { detail: {name: tag}, bubbles: true }));
                });
                this._pnltags.appendChild(btntag);
            }
        }
        else if (name == "title")
            this._titlediv.textContent = newVal;
        else if (name == "url")
            this._btnvisit.href = newVal;
    }

}

customElements.define("ginggar-messagelistentry", MessageListEntry);
