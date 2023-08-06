/**
* @license
* SPDX-FileCopyrightText: © 2021 Josef Hahn
* SPDX-License-Identifier: AGPL-3.0-only
*/

import {animateNode} from '../piweb/animation.js';


/**
* Animates the expansion of a node.
*/
export async function animateExpandNode(node) {
    node.style.maxHeight = 0;
    node.style.opacity = 0;
    node.style.display = "";
    if (await animateNode(node, "ginggar-nodeexpand")) {
        node.style.maxHeight = "";
        node.style.opacity = "";
    }
}

/**
* Animates the collapsing of a node.
*/
export async function animateCollapseNode(node) {
    node.style.maxHeight = `${node.getBoundingClientRect().height}px`;
    if (await animateNode(node, "ginggar-nodecollapse"))
        node.style.display = "none";
}
