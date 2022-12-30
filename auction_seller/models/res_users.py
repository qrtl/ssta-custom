# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class Users(models.Model):
    _inherit = "res.users"

    is_auction_seller = fields.Boolean(
        compute="_compute_is_auction_seller",
        inverse="_inverse_is_auction_seller",
    )

    def _compute_is_auction_seller(self):
        for user in self:
            user.is_auction_seller = False
            if user.has_group("auction_seller.group_auction_seller"):
                user.is_auction_seller = True

    def _inverse_is_auction_seller(self):
        group_auction_seller = self.env.ref("auction_seller.group_auction_seller")
        for user in self:
            if user.is_auction_seller:
                user.write({"groups_id": [(4, group_auction_seller.id)]})
            else:
                user.write({"groups_id": [(3, group_auction_seller.id)]})
