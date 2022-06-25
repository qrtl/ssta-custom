# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

import hashlib
import json

import odoo
from odoo import models
from odoo.http import request
from odoo.tools import ustr

from odoo.addons.web.controllers.main import HomeStaticTemplateHelpers


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        # Extending the standard method, only to replicate the session update for
        # internal users described in below link for auction users:
        # https://github.com/odoo/odoo/blob/39c678a1ccb50d3a1871a4049a8df26427b27a3c/addons/web/models/ir_http.py#L65-L94  # noqa
        session_info = super().session_info()
        user = request.env.user
        mods = odoo.conf.server_wide_modules or []
        if self.env.user.has_group("base_auction.group_auction_user"):
            if request.db:
                mods = list(request.registry._init_modules) + mods
            qweb_checksum = HomeStaticTemplateHelpers.get_qweb_templates_checksum(debug=request.session.debug, bundle="web.assets_qweb")
            menus = request.env['ir.ui.menu'].load_menus(request.session.debug)
            ordered_menus = {str(k): v for k, v in menus.items()}
            menu_json_utf8 = json.dumps(ordered_menus, default=ustr, sort_keys=True).encode()
            session_info['cache_hashes'].update({
                "load_menus": hashlib.sha512(menu_json_utf8).hexdigest()[:64], # sha512/256
                "qweb": qweb_checksum,
            })
            session_info.update({
                # current_company should be default_company
                "user_companies": {
                    'current_company': user.company_id.id,
                    'allowed_companies': {
                        comp.id: {
                            'id': comp.id,
                            'name': comp.name,
                            'sequence': comp.sequence,
                        } for comp in user.company_ids
                    },
                },
                "show_effect": True,
                "display_switch_company_menu": user.has_group('base.group_multi_company') and len(user.company_ids) > 1,
            })
        return session_info
