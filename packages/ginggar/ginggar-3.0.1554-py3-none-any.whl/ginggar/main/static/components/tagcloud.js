/**
* @license
* SPDX-FileCopyrightText: © 2021 Josef Hahn
* SPDX-License-Identifier: AGPL-3.0-only
*/

import {backend} from '../backend/common.js';
import {baseStylesRef} from '../piweb/styling.js';


const tagCloudTemplate = document.createElement("template");
tagCloudTemplate.innerHTML = `
    ${baseStylesRef()}
    <style>
        :host {
            display: block;
        }
        ginggar-tagbutton, ginggar-tagcheckbutton {
            float: left;
            margin: var(--sl-spacing-xxx-small);
        }
        #clearfloat {
            clear: both;
        }
        #btnnewtag {
            margin-top: 1rem;
            display: none;
        }
        #btnnewtag.visible {
            display: inline-block;
        }
        #btnnewtag::part(base) {
            height: 100%;
        }
        #btnnewtag::part(label) {
            padding: var(--sl-spacing-xx-small) var(--sl-spacing-medium) var(--sl-spacing-xx-small) 0;
        }
        #btnnewtag div {
            display: grid;
            grid-template-columns: auto auto;
        }
        #btnnewtag input {
            width: 10rem;
            background: #00000066;
            border: none;
            color: #d9deec;
            font-size: 1.3em;
        }
        #btnnewtag input::placeholder {
            color: #94adf3;
        }
        #btnnewtag sl-icon {
            font-size: 2.3rem;
        }
    </style>
    <div id="main"></div>
    <div id="clearfloat"></div>
    <ginggar-tagbutton id="btnnewtag">
        <div>
            <input id="edtnewtag" placeholder="New tag"></input>
            <sl-icon name="plus"></sl-icon>
        </div>
    </sl-button>
`;

/**
* A list of tags in cloud like presentation.
*/
export class TagCloud extends HTMLElement {

    constructor() {
        super();
        var self = this;
        this._shadow = this.attachShadow({mode: "open"});
        this._shadow.appendChild(tagCloudTemplate.content.cloneNode(true));
        this._maindiv = this._shadow.getElementById("main");
        this._btnnewtag = this._shadow.getElementById("btnnewtag");
        this._edtnewtag = this._shadow.getElementById("edtnewtag");
        this._edtnewtag.addEventListener("click", (event) => {
            event.stopPropagation();
            return;
        });
        function _addNewTag() {
            self.checkedTags = self.checkedTags.concat(self._edtnewtag.value);
            self._edtnewtag.value = "";
        }
        this._edtnewtag.addEventListener("keydown", (event) => {
            if (event.key == "Enter" || event.key == " ") {
                _addNewTag();
                event.stopPropagation();
            }
        });
        this._btnnewtag.addEventListener("click", (event) => {
            if (!self._edtnewtag.value) {
                event.stopPropagation();
                return;
            }
            _addNewTag();
        });
        this._checkedtags = [];
        this._tags = [];
        this._refreshIntervalToken = undefined;
        this.refresh();
        this._isdomconnected = false;
        this._isautorefresh = false;
    }

    static get observedAttributes() {
        return ["allows-new", "auto-refresh"];
    }

    /**
    * If this tag cloud allows adding new tags (i.e. ones that are not part of the existing cloud).
    */
    get allowsNew() {
        return this.hasAttribute("allows-new");
    }

    set allowsNew(v) {
        if (v)
            this.setAttribute("allows-new", v);
        else
            this.removeAttribute("allows-new");
    }

    /**
    * If this tag cloud automatically refreshes in background.
    */
    get autoRefresh() {
        return this.hasAttribute("auto-refresh");
    }

    set autoRefresh(v) {
        if (v)
            this.setAttribute("auto-refresh", v);
        else
            this.removeAttribute("auto-refresh");
    }

    _handleRefresh() {
        if (this._isdomconnected && this._isautorefresh) {
            if (!this._refreshIntervalToken)
                this._refreshIntervalToken = setInterval(this.refresh.bind(this), 30*1000);
        }
        else {
            if (this._refreshIntervalToken) {
                clearInterval(this._refreshIntervalToken);
                this._refreshIntervalToken = undefined;
            }
        }
    }

    connectedCallback() {
        this._isdomconnected = true;
        this._handleRefresh();
    }

    disconnectedCallback() {
        this._isdomconnected = false;
        this._handleRefresh();
    }

    /**
    * Asks the backend for an update on tags.
    */
    async refresh() {
        this._tags = await backend.listTags();
        this._render();
    }

    _render() {
        var self = this;
        function _createTagButton(tag, isChecked, size) {
            let btntag = document.createElement("ginggar-tagcheckbutton");
            btntag.textContent = tag;
            btntag.style.setProperty("--size", `${size||1}rem`);
            btntag.isChecked = isChecked;
            self._maindiv.appendChild(btntag);
        }
        this._maindiv.innerHTML = "";
        var checkedtags = new Set(this._checkedtags);
        for (let tag of this._tags)
            _createTagButton(tag.name, checkedtags.delete(tag.name), tag.size);
        for (let tag of checkedtags)
            _createTagButton(tag, true);
    }

    /**
    * Returns all checked tags as list of string.
    */
    get checkedTags() {
        var result = [];
        for (let btntag of this._maindiv.children) {
            if (btntag.isChecked)
                result.push(btntag.textContent);
        }
        return result;
    }

    set checkedTags(tags) {
        this._checkedtags = tags.map(x => x.trim()).filter(x => x);
        this._render();
    }

    attributeChangedCallback(name, oldVal, newVal) {
        if (name == "allows-new") {
            if (newVal !== null)
                this._btnnewtag.classList.add("visible");
            else
                this._btnnewtag.classList.remove("visible");
        }
        else if (name == "auto-refresh") {
            this._isautorefresh = newVal !== null;
            this._handleRefresh();
        }
    }

}

customElements.define("ginggar-tagcloud", TagCloud);


const tagButtonTemplate = document.createElement("template");
tagButtonTemplate.innerHTML = `
    ${baseStylesRef()}
    <style>
        :host {
            --size: 1rem;
            --backgroundpattern: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADkAAAAcCAYAAADbeRcAAAAABmJLR0QAAAAAAAD5Q7t/AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4AofADUdWW1AJQAAABl0RVh0Q29tbWVudABDcmVhdGVkIHdpdGggR0lNUFeBDhcAAADrSURBVFjD3dY7CoNgEATgySqSpBDBpPqxtRI8gvf1NoqtlZ0g2Bg1SJJO8vBdxdl6YfjYKfYQhuEFGybLMj1JklNRFMbcrog8lVKN7/uNZVmPLXllWUoURcc8z49t2x7m9m3bvnueVzuO0wk7EACEHbgauUfgKuRegYuRewYuQu4dOItkAE4iWYCjSCbgIJIN+INkBH4gWYE9khkIAMIOBABNKXVlBsZxbAg7ME3Ts7ADq6rShB04+daxAEeRTMBBJBsQAPQhYBAEt61h/wb8uOT7BZmAPZKxol8N5QYCgLADTdPshB3oum79AhgfDkn8Gxf9AAAAAElFTkSuQmCC');
            display: inline-block;
        }
        #button {
            font-size: var(--size);
            border-radius: 0.5rem;
            letter-spacing: -0.05em;
            border: 0.125rem solid #6c4904;
            color: #f9eed0;
            background: var(--backgroundpattern), #7d5a07;
            transition: background var(--sl-transition-slow), color var(--sl-transition-slow);
        }
        #button.unchecked {
            background: var(--backgroundpattern), #f9eed2;
            border: 0.125rem solid #bb9f4c;
            color: #75683e;
        }
    </style>
    <button id="button">
        <slot></slot>
    </button>
`;

/**
* A button for a tag (i.e. with tag specific styling).
*/
export class TagButton extends HTMLElement {

    constructor() {
        super();
        this._shadow = this.attachShadow({ mode: "open" });
        this._shadow.appendChild(tagButtonTemplate.content.cloneNode(true));
        this._button = this._shadow.getElementById("button");
    }

}

customElements.define("ginggar-tagbutton", TagButton);


/**
* Like TagButton, but checkable.
*/
export class TagCheckButton extends TagButton {

    constructor() {
        super();
        var self = this;
        this._button.addEventListener("click", () => { self.isChecked = !self.isChecked; });
        this.isChecked = true;
        this.isChecked = false;
    }

    static get observedAttributes() {
        return ["is-checked"].concat(super.observedAttributes);
    }

    /**
    * If this tag button is in checked state.
    */
    get isChecked() {
        return this.hasAttribute("is-checked");
    }

    set isChecked(v) {
        if (v)
            this.setAttribute("is-checked", v);
        else
            this.removeAttribute("is-checked");
    }

    attributeChangedCallback(name, oldVal, newVal) {
        if (name == "is-checked") {
            if (newVal !== null)
                this._button.classList.remove("unchecked");
            else
                this._button.classList.add("unchecked");
        }
        else
            super.attributeChangedCallback(name, oldVal, newVal);
    }

}

customElements.define("ginggar-tagcheckbutton", TagCheckButton);
