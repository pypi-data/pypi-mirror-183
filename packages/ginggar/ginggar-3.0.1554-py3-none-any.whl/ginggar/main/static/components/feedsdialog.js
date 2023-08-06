/**
* @license
* SPDX-FileCopyrightText: © 2021 Josef Hahn
* SPDX-License-Identifier: AGPL-3.0-only
*/

import {backend} from '../backend/common.js';
import {messageDialog} from '../piweb/conversationdialog.js';
import {baseStylesRef} from '../piweb/styling.js';


const dialogTemplate = document.createElement("template");
dialogTemplate.innerHTML = `
    ${baseStylesRef()}
    <style>
        #btnnew {
            margin: var(--sl-spacing-x-large) 0 0 30%;
            transition: max-height var(--sl-transition-slow);
            overflow: hidden;
            padding: 0.4rem;
            max-height: 5rem;
            opacity: 1;
        }
        sl-dialog.showformnew #btnnew {
            max-height: 0;
            opacity: 0;
        }
        sl-dialog.showformnew #formnew {
            max-height: 80rem;
            opacity: 1;
        }
        #formnew {
            max-height: 0;
            opacity: 0;
            transition: max-height var(--sl-transition-slow);
            overflow: hidden;
            padding: 0.4rem;
        }
        #btnnew sl-icon {
            font-size: 3rem;
        }
        #feedlist {
            display: grid;
            margin-top: var(--sl-spacing-medium);
        }
        #feedlist-isempty,
        #feedlist-list,
        #feedlist-spinner {
            grid-row: 1;
            grid-column: 1;
            opacity: 0;
            pointer-events: none;
            transition: opacity var(--sl-transition-slow);
        }
        #feedlist.isempty #feedlist-isempty,
        #feedlist.isnonempty #feedlist-list,
        #feedlist.isloading #feedlist-spinner {
            opacity: 1;
            pointer-events: initial;
        }
        #feedlist h3 {
            margin: var(--sl-spacing-medium) 0 0 0;
            padding: 0;
        }
        #feedlist .details {
            color: #00000077;
        }
        #feedlist .details span {
            margin-left: var(--sl-spacing-x-large);
        }
    </style>
    <sl-dialog label="Feeds">
        <div class="dialoghead">
            Manage the feeds you want to receive messages from.
        </div>
        <div id="feedlist">
            <div id="feedlist-isempty">
                <sl-alert type="primary" open>
                    <sl-icon slot="icon" name="link-45deg"></sl-icon>
                    <strong>You currently have no feeds configured</strong><br>
                    Why not add one now?
                </sl-alert>
            </div>
            <div id="feedlist-list">
            </div>
            <sl-spinner id="feedlist-spinner"></sl-spinner>
        </div>
        <sl-button type="primary" size="large" circle id="btnnew">
            <sl-icon name="plus"></sl-icon>
        </sl-button>
        <sl-form id="formnew">
            <h4>Add new feed</h4>
            <sl-input id="formnew-edturl" label="Source address" required clearable>
                <div slot="help-text">
                    Find an RSS, RDF or Atom address on the website of your source or ask them for it. It should
                    start with "http://" or "https://".
                </div>
            </sl-input><br/>
            <sl-input id="formnew-edtname" label="Name" required clearable>
                <div slot="help-text">
                    Choose whatever is convenient for you.
                </div>
            </sl-input><br/>
            <sl-select id="formnew-edtinterval" label="Update interval" value="30" required hoist>
                <sl-menu-item value="2">2 minutes</sl-menu-item>
                <sl-menu-item value="5">5 minutes</sl-menu-item>
                <sl-menu-item value="15">15 minutes</sl-menu-item>
                <sl-menu-item value="30">30 minutes</sl-menu-item>
                <sl-menu-item value="60">60 minutes</sl-menu-item>
                <div slot="help-text">
                    New messages will be fetched from the source in this interval.
                </div>
            </sl-select>
            <sl-button type="primary" submit>Submit</sl-button>
        </sl-form>
        <sl-button slot="footer" type="primary" id="btnclose">Close</sl-button>
    </sl-dialog>
`;

/**
* The Feeds dialog.
*/
export class FeedsDialog extends HTMLElement {

    constructor() {
        super();
        var self = this;
        this._shadow = this.attachShadow({ mode: "open" });
        this._shadow.appendChild(dialogTemplate.content.cloneNode(true));
        this._dialog = this._shadow.querySelector("sl-dialog");
        this._feedlistIsempty = this._shadow.getElementById("feedlist-isempty");
        this._feedlistSpinner = this._shadow.getElementById("feedlist-spinner");
        this._feedlistList = this._shadow.getElementById("feedlist-list");
        this._feedlist = this._shadow.getElementById("feedlist");
        this._btnnew = this._shadow.getElementById("btnnew");
        this._btnclose = this._shadow.getElementById("btnclose");
        this._formnew = this._shadow.getElementById("formnew");
        this._edtname = this._shadow.getElementById("formnew-edtname");
        this._edturl = this._shadow.getElementById("formnew-edturl");
        this._edtinterval = this._shadow.getElementById("formnew-edtinterval");
        this._btnnew.addEventListener("click", () => {
            self._setFormNewVisibility(true);
        });
        this._btnclose.addEventListener("click", () => {
            self._dialog.hide();
        });
        this._edturl.addEventListener("sl-input", () => {
            var name = self._edturl.value;
            try {
                name = new URL(name).host;
                var domainparts = name.split(".");
                name = domainparts[domainparts.length-2];
            }
            catch (e) {
            }
            self._edtname.value = name;
        });
        this._formnew.addEventListener("sl-submit", async () => {
            await backend.addFeed(self._edtname.value, self._edturl.value, self._edtinterval.value);
            self._reload();
        });
        this._reload();
    }

    async _reload() {
        var self = this;
        this._feedlist.className = "isloading";
        this._feedlistList.innerHTML = "";
        this._setFormNewVisibility(false);
        var feedsdata = await backend.listFeeds();
        if (feedsdata.length > 0) {
            this._feedlist.className = "isnonempty";
            for (let feeddata of feedsdata) {
                var lblname = document.createElement("h3");
                lblname.textContent = feeddata.name;
                this._feedlistList.appendChild(lblname);
                var lblurl = document.createElement("div");
                lblurl.textContent = feeddata.url;
                this._feedlistList.appendChild(lblurl);
                var pnldetails = document.createElement("div");
                pnldetails.className = "details";
                var btnremove = document.createElement("sl-button");
                btnremove.circle = true;
                btnremove.innerHTML = '<sl-icon name="trash" size="small"></sl-icon>';
                pnldetails.appendChild(btnremove);
                var lblupdateinterval = document.createElement("span");
                lblupdateinterval.innerHTML = `
                    <sl-icon name="hourglass-top"></sl-icon>
                    ${feeddata.updateInterval} minutes`;
                pnldetails.appendChild(lblupdateinterval);
                this._feedlistList.appendChild(pnldetails);
                btnremove.addEventListener("click", async () => {
                    if ((await messageDialog({
                        message: `Do you really want to remove the feed '${feeddata.name}'?`,
                        buttons: ["No", "Yes"],
                        defaultCancelAnswer: 0,
                        defaultAcceptAnswer: 1
                    })) == 1) {
                        await backend.disableFeed(feeddata.id);
                        self._reload();
                    }
                });
            }
        }
        else {
            this._feedlist.className = "isempty";
            this._setFormNewVisibility(true);
        }
    }

    _setFormNewVisibility(v) {
        this._edtname.value = "";
        this._edturl.value = "";
        if (v)
            this._dialog.classList.add("showformnew");
        else
            this._dialog.classList.remove("showformnew");
    }

}

customElements.define("ginggar-feedsdialog", FeedsDialog);
