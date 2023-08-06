/**
* @license
* SPDX-FileCopyrightText: © 2021 Josef Hahn
* SPDX-License-Identifier: AGPL-3.0-only
*/

import {tagStringToTagList} from '../backend/common.js';
import {messageDialog} from '../piweb/conversationdialog.js';


/**
* Shows a tag dialog (a question text and a tag cloud for single selection).
*/
export async function tagDialog(cfg) {
    var tagcloud = document.createElement("ginggar-tagcloud");
    tagcloud.addEventListener("click", (event) => {
        if (tagcloud.checkedTags.length > 0)
            tagcloud._dialogresult = 1;
    });
    cfg.contentnodes = [tagcloud, ...(cfg.contentnodes || [])];
    cfg.buttons = ["Cancel"];
    cfg.defaultCancelAnswer = 0;
    if (await messageDialog(cfg))
        return tagcloud.checkedTags[0];
}

/**
* Shows a tags dialog (a question text and a tag cloud for multi selection).
*/
export async function tagsDialog(cfg) {
    var tagcloud = document.createElement("ginggar-tagcloud");
    tagcloud.checkedTags = tagStringToTagList(cfg.checkedTags || "");
    tagcloud.allowsNew = cfg.allowNewTags;
    cfg.contentnodes = [tagcloud, ...(cfg.contentnodes || [])];
    cfg.buttons = ["Cancel", "OK"];
    cfg.defaultCancelAnswer = 0;
    var elements = [tagcloud];
    if ((await messageDialog(cfg)) == 1)
        return tagcloud.checkedTags;
}
