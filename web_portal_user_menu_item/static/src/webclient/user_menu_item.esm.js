/** @odoo-modules */

import {registry} from "@web/core/registry";
import {preferencesItem} from "@web/webclient/user_menu/user_menu_items";
import {browser} from "@web/core/browser/browser";

export function ProtalUserMenu(env) {
    return Object.assign({}, preferencesItem(env), {
        type: "item",
        id: "portal",
        description: env._t("My Potal account"),
        callback: () => {
            browser.location.href = "/my";
        },
        sequence: 60,
    });
}

registry.category("user_menuitems").add("portal", ProtalUserMenu, {force: true});
