/**
* @license
* SPDX-FileCopyrightText: © 2021 Josef Hahn
* SPDX-License-Identifier: AGPL-3.0-only
*/

import {backend, getGinggarContextValue, subsite} from '../backend/common.js';
import * as messagesources from '../backend/messagesources.js';
import {userConfiguration} from '../backend/userconfiguration.js';
import {tagDialog, tagsDialog} from '../components/conversationdialog.js';
import {animateNode} from '../piweb/animation.js';
import {choiceDialog, inputDialog, messageDialog} from '../piweb/conversationdialog.js';
import {showShoelaceDialog} from '../piweb/dialog.js';


class MyMessageSourceListener extends messagesources.MessageSourceListener {

    constructor(messagelist, tagcloud) {
        super();
        this._messagelist = messagelist;
        this._tagcloud = tagcloud;
    }

    messageFilterChanged(messageSource, messageFilter) {
        var tags = [];
        for (let innerFilter of messageFilter?.innerFilters || []) {
            if (innerFilter.tag)
                tags.push(innerFilter.tag);
        }
        this._tagcloud.checkedTags = tags;
    }

    resetList(messageSource) {
        this._messagelist.reset();
    }

    messageArrived(messageSource, message) {
        this._messagelist.addMessage(message);
    }

    messageChanged(messageSource, message) {
        this._messagelist.changeMessage(message);
    }

    messageRemoved(messageSource, msgid) {
        this._messagelist.removeMessage(msgid);
    }

    beginRequestingMessages(messageSource, isUpdate) {
        this._messagelist.noMessagesInfo = (messageSource.messageFilter
            ? "There are no messages that match your current filter criteria."
            : "There are no messages.");
        if (!isUpdate)
            this._messagelist.isLoading = true;
    }

    endRequestingMessages(messageSource) {
        this._messagelist.isLoading = false;
    }

}

const messagelist = document.getElementById("panemessagelist-messagelist");
const btnmainmenu = document.getElementById("btnmainmenu");
const menu = document.getElementById("mainmenu");
const menubtnfiltering = document.getElementById("mainmenu-btnfiltering");
const menubtnfeeds = document.getElementById("mainmenu-btnfeeds");
const menubtnsettings = document.getElementById("mainmenu-btnsettings");
const menubtnadminpanel = document.getElementById("mainmenu-btnadminpanel");
const menubtnhelp = document.getElementById("mainmenu-btnhelp");
const menubtnlogout = document.getElementById("mainmenu-btnlogout");
const panes = document.getElementById("panes");
const panemessagelist = document.getElementById("panemessagelist");
const panefiltering = document.getElementById("panefiltering");
const panefilteringbtnback = document.getElementById("panefiltering-btnback");
const tagcloud = document.getElementById("panefiltering-tagcloud");
const filteringmenu = document.getElementById("panefiltering-menu");
const messagesource = new messagesources.MessageSource(new MyMessageSourceListener(messagelist, tagcloud));
filteringmenu.addEventListener("sl-select", async (event) => {
    if (event.detail.item.value == "clearfilter")
        messagesource.messageFilter = undefined;
    else if (event.detail.item.value == "switchsortorder") {
        messagesource.reverseSortOrder = !messagesource.reverseSortOrder;
        userConfiguration.setValue("reverseSortOrder", messagesource.reverseSortOrder);
    }
    else if (event.detail.item.value == "savefilter") {
        var chkdefault = document.createElement("sl-checkbox");
        chkdefault.textContent = "Use this also as my default after login";
        var filtername = await inputDialog({
            message: "Please choose a filter name.\n\n"
                     + "You will find your new filter by that name in the filter list later on.",
            contentnodes: [chkdefault]
        });
        if (filtername) {
            backend.storeFilter(filtername, messagesource.messageFilter?.toFilterString());
            if (chkdefault.checked)
                userConfiguration.setValue("defaultFilter", filtername);
        }
    }
    else if (event.detail.item.value == "loadfilter") {
        var filters = await backend.listFilters();
        if (filters.length == 0)
            return messageDialog({message: "There are currently no stored filters."});
        var ifilter = await choiceDialog({
            message: "Please choose a filter to load.",
            choices: filters.map(x => x.name)
        });
        if (ifilter !== undefined)
            messagesource.messageFilter = messagesources.MessageSource.getMessageFilterForFilterTuple(
                filters[ifilter].filterTuple);
    }
    else if (event.detail.item.value == "removefilter") {
        var filters = await backend.listFilters();
        if (filters.length == 0)
            return messageDialog({message: "There are currently no stored filters."});
        var ifilter = await choiceDialog({
            message: "Please choose a filter to remove.",
            choices: filters.map(x => x.name)
        });
        if (ifilter !== undefined)
            await backend.removeFilter(filters[ifilter].name);
    }
    else if (event.detail.item.value == "removetag") {
        var tag = await tagDialog({message: "Please choose a tag to remove."});
        if (tag !== undefined) {
            await backend.removeTag(tag);
            tagcloud.refresh();
        }
    }
    else if (event.detail.item.value == "tagpropagations")
        showShoelaceDialog("ginggar-tagpropagationdialog");
});
messagelist.addEventListener("remove", async (event) => {
    await backend.removeMessage(event.detail.msgid);
});
messagelist.addEventListener("favorite", async (event) => {
    await backend.favoriteMessage(event.detail.msgid, event.detail.isFavorite);
    tagcloud.refresh();
});
messagelist.addEventListener("tags", async (event) => {
    var tags = await tagsDialog({
        message: `Tag the article '${event.detail.msgtitle}' here.`,
        checkedTags: event.detail.msgtags,
        allowNewTags: true
    });
    if (tags !== undefined) {
        await backend.setTagsForMessage(event.detail.msgid, tags);
        tagcloud.refresh();
    }
});
messagelist.addEventListener("tagselected", (event) => {
    messagesource.messageFilter = new messagesources.AndMessageFilter(
        [new messagesources.TagMessageFilter(event.detail.name)]);
});
messagelist.addEventListener("seen", (event) => {
    backend.markMessageAsSeen(event.detail.msgid);
});
tagcloud.addEventListener("click", () => {
    var tags = tagcloud.checkedTags;
    messagesource.messageFilter = (tags.length > 0) ? new messagesources.AndMessageFilter(
                        tags.map(tag => new messagesources.TagMessageFilter(tag))) : undefined;
});
btnmainmenu.addEventListener("click", (event) => { menu.show(); });
menubtnfiltering.addEventListener("click", (event) => {
    menu.hide();
    switchTo(false);
});
menubtnfeeds.addEventListener("click", (event) => {
    menu.hide();
    showShoelaceDialog("ginggar-feedsdialog");
});
menubtnsettings.addEventListener("click", (event) => {
    menu.hide();
    showShoelaceDialog("ginggar-settingsdialog");
});
menubtnadminpanel.addEventListener("click", (event) => {
    menu.hide();
    window.open(`${subsite}admin`, "_blank");
});
menubtnhelp.addEventListener("click", (event) => {
    menu.hide();
    window.open(`${subsite}static/readme.pdf`, "_blank");
});
menubtnlogout.addEventListener("click", async (event) => {
    menu.hide();
    await backend.logout();
    location.href = location.href;
});
window.switchTo = function(v) {
    var onnode = v ? panemessagelist : panefiltering;
    var offnode = v ? panefiltering : panemessagelist;
    var onclass = v ? "showmessagelist" : "showfiltering";
    var offclass = v ? "showfiltering" : "showmessagelist";
    var animationduration = getComputedStyle(document.body).getPropertyValue("--sl-transition-slow");
    animateNode(onnode, "ginggar-fadein", animationduration);
    panes.classList.add(onclass);
    (async () => {
        if (await animateNode(offnode, "ginggar-fadeout", animationduration)) {
            panes.classList.remove(offclass);
        }
    })();
}
panefilteringbtnback.addEventListener("click", () => { switchTo(true); });
switchTo(true);
userConfiguration.getValue("onuiinitialized").then(v => v ? eval(`(${v})`)() : undefined);
userConfiguration.addListener("noanimations", (v) => {
    if (v)
        document.body.classList.add("ginggar-noanimations");
    else
        document.body.classList.remove("ginggar-noanimations");
});
if (getGinggarContextValue("firstlogin")) {
    var firstloginpanel = document.createElement("ginggar-firstloginpanel");
    document.body.appendChild(firstloginpanel);
    firstloginpanel.show();
}
if (getGinggarContextValue("singleusermode"))
    document.body.classList.add("ginggar-singleusermode");
if (!getGinggarContextValue("issuperuser"))
    document.body.classList.add("ginggar-noadminpanel");
document.addEventListener("focusout", () => {
    setTimeout(() => {
        if (document.activeElement == document.body)
            messagelist.focus();
    });
});
messagelist.focus();
(async () => {
    var [filters, defaultFilterName, reverseSortOrder] = await Promise.all(
        [backend.listFilters(), userConfiguration.getValue("defaultFilter"),
         userConfiguration.getValue("reverseSortOrder")]);
    var defaultFilter;
    if (defaultFilterName) {
        var defaultFilterTuple = filters.find(f => f.name == defaultFilterName)?.filterTuple;
        if (defaultFilterTuple)
            defaultFilter = messagesources.MessageSource.getMessageFilterForFilterTuple(defaultFilterTuple);
    }
    messagesource.reverseSortOrder = reverseSortOrder;
    messagesource.messageFilter = defaultFilter;
})();
