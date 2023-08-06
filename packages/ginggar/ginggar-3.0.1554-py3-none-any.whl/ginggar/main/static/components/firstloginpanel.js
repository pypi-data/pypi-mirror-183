/**
* @license
* SPDX-FileCopyrightText: © 2021 Josef Hahn
* SPDX-License-Identifier: AGPL-3.0-only
*/

import {baseStylesRef} from '../piweb/styling.js';


const panelTemplate = document.createElement("template");
panelTemplate.innerHTML = `
    ${baseStylesRef()}
    <sl-drawer placement="bottom" label="Welcome to Ginggar!">
        <p>
            You can organize and read your favorite
            <a style="cursor: help" target="_blank" rel="noopener" href="https://en.wikipedia.org/wiki/Web_feed">web
            feeds</a> here.
        </p>
        <p>
            Open the menu from the header bar and add some feeds. You will then see messages from those feeds here,
            so you can read and manage them.
        </p>
        <sl-button type="primary" id="btnclose">Got it.</sl-button>
    </sl-drawer>
`;

/**
* The info panel to be shown at first login.
*
* Is invisible at first and needs show() to be called.
*/
export class FirstLoginPanel extends HTMLElement {

    constructor() {
        super();
        var self = this;
        this._shadow = this.attachShadow({ mode: "open" });
        this._shadow.appendChild(panelTemplate.content.cloneNode(true));
        this._drawer = this._shadow.querySelector("sl-drawer");
        this._shadow.getElementById("btnclose").addEventListener("click", () => { self._drawer.hide(); });
    }

    /**
    * Shows the panel.
    */
    show() {
        this._drawer.show();
    }

}

customElements.define("ginggar-firstloginpanel", FirstLoginPanel);
