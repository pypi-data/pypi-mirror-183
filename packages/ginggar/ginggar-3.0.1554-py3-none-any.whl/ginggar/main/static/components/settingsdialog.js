/**
* @license
* SPDX-FileCopyrightText: © 2021 Josef Hahn
* SPDX-License-Identifier: AGPL-3.0-only
*/

import {backend, getGinggarContextValue} from '../backend/common.js';
import {userConfiguration} from '../backend/userconfiguration.js';
import {showShoelaceDialog} from '../piweb/dialog.js';
import {baseStylesRef} from '../piweb/styling.js';


const dialogTemplate = document.createElement("template");
dialogTemplate.innerHTML = `
    ${baseStylesRef()}
    <style>
        #pnlscripting-handlers {
            margin: var(--sl-spacing-medium);
            display: grid;
            grid-template-columns: auto;
        }
        .not-backenduserscriptingavailable #btnhandleronnewmsg,
        .not-backenduserscriptingavailable #btnhandlerontagassigned {
            display: none;
        }
    </style>
    <sl-dialog label="Settings">
        <div class="dialoghead">
            Customize some Ginggar settings here.
        </div>
        <sl-details summary="General" open>
            <div id="pnlgeneral"></div>
        </sl-details>
        <sl-details summary="Scripting">
            <div id="pnlscripting">
                You can customize many aspects of Ginggar by scripting.<br/><br/>
                This is a very advanced feature, which you will not get right without reading the manual.
                <div id="pnlscripting-handlers">
                    <sl-button id="btnhandleronnewmsg">Implement 'on new message' handler</sl-button><br/>
                    <sl-button id="btnhandlerontagassigned">Implement 'tag assigned' handler</sl-button><br/>
                    <sl-button id="btnhandleronuiinit">Implement 'user interface initialize' handler</sl-button><br/>
                </div>
            </div>
        </sl-details>
        <sl-button slot="footer" type="primary" id="btnclose">Close</sl-button>
    </sl-dialog>
`;

/**
* The Settings dialog.
*/
export class SettingsDialog extends HTMLElement {

    constructor() {
        super();
        var self = this;
        this._shadow = this.attachShadow({mode: "open"});
        this._shadow.appendChild(dialogTemplate.content.cloneNode(true));
        this._dialog = this._shadow.querySelector("sl-dialog");
        this._pnlgeneral = this._shadow.getElementById("pnlgeneral");
        this._pnlscripting = this._shadow.getElementById("pnlscripting");
        this._btnclose = this._shadow.getElementById("btnclose");
        this._btnhandleronnewmsg = this._shadow.getElementById("btnhandleronnewmsg");
        this._btnhandlerontagassigned = this._shadow.getElementById("btnhandlerontagassigned");
        this._btnhandleronuiinit = this._shadow.getElementById("btnhandleronuiinit");
        this._btnclose.addEventListener("click", (event) => {
            self._dialog.hide();
        });
        this._btnhandleronnewmsg.addEventListener("click", (event) => {
            self._change_script("onnewmessage");
        });
        this._btnhandlerontagassigned.addEventListener("click", (event) => {
            self._change_script("ontagset");
        });
        this._btnhandleronuiinit.addEventListener("click", (event) => {
            self._change_script("onuiinitialized");
        });
        this._reload_basicsettings();
        if (!getGinggarContextValue("backenduserscriptingavailable"))
            this._dialog.classList.add("not-backenduserscriptingavailable");
    }

    async _reload_basicsettings() {
        var self = this;
        async function _setSetting(k, v) {
            await backend.setConfigValue(k, v);
            self._reload_basicsettings();
        };
        this._pnlgeneral.innerHTML = "";
        var plist = document.createElement("ul");
        this._pnlgeneral.appendChild(plist);
        function newplistentry() {
            var result = document.createElement("li");
            plist.appendChild(result);
            return result;
        }
        var elemAnimation = newplistentry();
        var currentValue = async () => userConfiguration.getValue("noanimations");
        var txt = (await currentValue()
                        ? "The user interface is set up to be not animated."
                        : "The user interface is set up to be animated.");
        elemAnimation.innerHTML = `${txt} <sl-button size='small'>toggle</sl-button>`;
        elemAnimation.querySelector("sl-button").addEventListener("click", async () => {
            _setSetting("noanimations", !(await currentValue()));
        });
    }

    async _change_script(handlername) {
        var dialog = showShoelaceDialog("ginggar-editscriptpopupdialog");
        dialog.value = (await userConfiguration.getValue(handlername)) || this._scriptdefaults[handlername];
        dialog._dialog.addEventListener("sl-hide", async () => {
            if (dialog.isAccepted)
                await backend.setConfigValue(handlername, dialog.value);
        });
    }

    _scriptdefaults = {
        "onnewmessage":
            "def onnewmessage(message):\n" +
            "    #if 'space' in message.summary:\n" +
            "    #    message.add_tag('deepspace')\n" +
            "    #    message.save()\n" +
            "    pass\n",
        "ontagset":
            "def ontagset(message, tag):\n" +
            "    #if tag == 'deepspace':\n" +
            "    #    message.add_tag('favorite')\n" +
            "    #    message.save()\n" +
            "    #if tag == 'archive':\n" +
            "    #    if 'tuna' in message.summary:\n" +
            "    #        message.delete_later()\n" +
            "    #    else:\n" +
            "    #        store_somehow_to_pdf(message.url)\n" +
            "    pass\n",
        "onuiinitialized":
            "function onUiInitialized() {\n" +
            "    //document.body.style.filter = 'hue-rotate(190deg)';\n" +
            "}\n"
    };

}

customElements.define("ginggar-settingsdialog", SettingsDialog);

const editScriptPopupTemplate = document.createElement('template');
editScriptPopupTemplate.innerHTML = `
    ${baseStylesRef()}
    <sl-dialog label="Edit script">
        <sl-textarea resize="auto" id="edt"></sl-textarea>
        <sl-button slot="footer" id="btnclose">Cancel</sl-button>
        <sl-button slot="footer" type="primary" id="btnsave">Save</sl-button>
    </sl-dialog>
`;

/**
* Popup dialog for editing scripts.
*/
export class EditScriptPopupDialog extends HTMLElement {

    constructor() {
        super();
        var self = this;
        this._isaccepted = false;
        this._shadow = this.attachShadow({ mode: "open" });
        this._shadow.appendChild(editScriptPopupTemplate.content.cloneNode(true));
        this._dialog = this._shadow.querySelector("sl-dialog");
        this._btnclose = this._shadow.getElementById("btnclose");
        this._btnsave = this._shadow.getElementById("btnsave");
        this._edt = this._shadow.getElementById("edt");
        this._btnclose.addEventListener("click", (event) => {
            self._dialog.hide();
        });
        this._btnsave.addEventListener("click", (event) => {
            self.value = self._edt.value;
            self._isaccepted = true;
            self._dialog.hide();
        });
    }

    /**
    * If the dialog was accepted (i.e. not cancelled).
    */
    get isAccepted() {
        return this._isaccepted;
    }

    static get observedAttributes() {
        return ['value'];
    }

    /**
    * The script text.
    */
    get value() {
        return this.getAttribute('value');
    }

    set value(v) {
        this.setAttribute('value', v);
    }

    attributeChangedCallback(name, oldVal, newVal) {
        if (name == 'value')
            this._edt.value = newVal;
    }

}

customElements.define("ginggar-editscriptpopupdialog", EditScriptPopupDialog);
