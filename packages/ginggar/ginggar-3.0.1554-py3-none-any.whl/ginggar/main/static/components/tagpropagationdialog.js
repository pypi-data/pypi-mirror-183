/**
* @license
* SPDX-FileCopyrightText: © 2021 Josef Hahn
* SPDX-License-Identifier: AGPL-3.0-only
*/

import {backend} from '../backend/common.js';
import {tagsDialog} from '../components/conversationdialog.js';
import {messageDialog} from '../piweb/conversationdialog.js';
import {baseStylesRef} from '../piweb/styling.js';


const dialogTemplate = document.createElement("template");
dialogTemplate.innerHTML = `
    ${baseStylesRef()}
    <style>
        #btnnew {
            margin: 1.25rem 0 0 30%;
            padding: 0.4rem;
        }
        #btnnew sl-icon {
            font-size: 3rem;
        }
        #rulelist sl-button {
            margin-left: var(--sl-spacing-x-small);
        }
    </style>
    <sl-dialog label="Tag propagation rules">
        <div class="dialoghead">
            Define tag propagation rules here.
            <p>
                Whenever a message gets some tags, those rules can automatically add further tags to that message.
                Example: "<span id="lblsamplerule"></span>"
            </p>
        </div>
        <div id="rulelist">
        </div>
        <sl-button type="primary" size="large" circle id="btnnew">
            <sl-icon name="plus"></sl-icon>
        </sl-button>
        <sl-button slot="footer" type="primary" id="btnclose">Close</sl-button>
    </sl-dialog>
`;

/**
* The Tag Propagations dialog.
*/
export class TagPropagationDialog extends HTMLElement {

    constructor() {
        super();
        var self = this;
        this._shadow = this.attachShadow({ mode: "open" });
        this._shadow.appendChild(dialogTemplate.content.cloneNode(true));
        this._dialog = this._shadow.querySelector("sl-dialog");
        this._rulelist = this._shadow.getElementById("rulelist");
        this._shadow.getElementById("lblsamplerule").textContent = this._toFriendlyRule(["cars"], ["transportation"]);
        var btnclose = this._shadow.getElementById("btnclose");
        var btnnew = this._shadow.getElementById("btnnew");
        btnclose.addEventListener("click", () => {
            self._dialog.hide();
        });
        btnnew.addEventListener("click", async () => {
            var iftags = await tagsDialog({
                message: "Please choose the tags that should be the condition part of the new rule.",
                allowNewTags: true
            });
            if (!iftags)
                return;
            var siftags = self._toFriendlyTags(iftags);
            var applyalsotags = await tagsDialog({
                message: `Please choose the tags that should be implied by ${siftags} in the new rule.`,
                allowNewTags: true
            });
            if (!applyalsotags)
                return;
            await backend.addTagPropagationRule(iftags, applyalsotags)
            self._reload();
        });
        this._reload();
    }

    _toFriendlyRule(iftags, applyalsotags) {
        if (iftags.length == 1 && applyalsotags.length == 1)
            var myphrase = "The tag #1 also implies #2.";
        else if (iftags.length != 1 && applyalsotags.length == 1)
            var myphrase = "The tags #1 also imply #2.";
        else if (iftags.length == 1 && applyalsotags.length != 1)
            var myphrase = "The tag #1 also implies #2.";
        else
            var myphrase = "The tags #1 also imply #2.";
        return myphrase.replace("#1", this._toFriendlyTags(iftags)).replace("#2", this._toFriendlyTags(applyalsotags));
    }

    _toFriendlyTags(taglist) {
        var quotedtags = taglist.map(x => `'${x}'`);
        if (quotedtags.length > 1) {
            var s = quotedtags.splice(0, quotedtags.length-1).join(", ");
            return `${s} and ${quotedtags[0]}`;
        }
        else
            return quotedtags.join("");
    }

    async _reload() {
        var self = this;
        var rules = await backend.listTagPropagationRules();
        if (rules.length == 0)
            this._rulelist.textContent = "You have not defined any tag propagation rules so far.";
        else {
            this._rulelist.innerHTML = "";
            var ullist = document.createElement("ul");
            this._rulelist.appendChild(ullist);
            for (let rule of rules) {
                var liitem = document.createElement("li");
                liitem.textContent = this._toFriendlyRule(rule.iftags, rule.applyalsotags);
                let btnremove = document.createElement("sl-button");
                btnremove.textContent = "Remove";
                btnremove.size = "small";
                btnremove.addEventListener("click", async () => {
                    if ((await messageDialog({
                        message: "Do you really want to delete this tag propagation rule?",
                        buttons: ["No", "Yes"],
                        defaultCancelAnswer: 0,
                        defaultAcceptAnswer: 1
                    })) == 1) {
                        await backend.removeTagPropagationRule(rule.id);
                        self._reload();
                    }
                });
                liitem.appendChild(btnremove);
                ullist.appendChild(liitem);
            }
        }
    }

}

customElements.define("ginggar-tagpropagationdialog", TagPropagationDialog);
