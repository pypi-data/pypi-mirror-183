/**
* @license
* SPDX-FileCopyrightText: © 2021 Josef Hahn
* SPDX-License-Identifier: AGPL-3.0-only
*/

import {backend, BackendListener} from './common.js';


/**
* User specific configuration. Can store arbitrary json-serializable objects for a (string) key.
*
* Stored on backend side in a persistent way.
*/
class UserConfiguration {

    constructor() {
        this._listeners = {};
        this._config = {};
        this._backendListener = new UserConfigurationBackendListener(this);
        backend.registerListener(this._backendListener);
    }

    /**
    * Adds a listener function for changes of a particular key.
    *
    * The handler function will directly be called with the current value as well.
    */
    async addListener(key, handler) {
        var listeners = this._listeners[key] = this._listeners[key] || [];
        listeners.push(handler);
        handler(await this.getValue(key));
    }

    /**
    * Returns a configuration value by key.
    */
    async getValue(key, defaultValue) {
        if (!this._config.hasOwnProperty(key))
            this._config[key] = await backend.getConfigValue(key, defaultValue);
        return this._config[key];
    }

    /**
    * Sets a configuration value by key.
    */
    async setValue(key, value) {
        this._changed(key, value);
        await backend.setConfigValue(key, value);
    }

    _changed(key, value) {
        if (this._config.hasOwnProperty(key) && this._config[key] === value)
            return;
        this._config[key] = value;
        for (let listener of (this._listeners[key] || []))
            listener(value);
    }

}

class UserConfigurationBackendListener extends BackendListener {

    constructor(userConfiguration) {
        super();
        this._userConfiguration = userConfiguration;
    }

    userConfigurationChanged(key, value) {
        this._userConfiguration._changed(key, value);
    }

}

/**
* The UserConfiguration.
*/
export const userConfiguration = new UserConfiguration();
