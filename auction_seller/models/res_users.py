# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class Users(models.Model):
    _inherit = "res.users"

    is_auction_seller_user = fields.Boolean(
        compute="_compute_is_auction_seller_user", inverse="_inverse_is_auction_seller_user"
    )

    def _compute_is_auction_seller_user(self):
        for user in self:
            user.is_auction_seller_user = False
            if user.has_group("auction_seller.group_auction_seller_user"):
                user.is_auction_seller_user = True

    def _inverse_is_auction_seller_user(self):
        group_auction_seller_user = self.env.ref("auction_seller.group_auction_seller_user")
        for user in self:
            if user.is_auction_seller_user:
                user.write({"groups_id": [(4, group_auction_seller_user.id)]})
            else:
                user.write({"groups_id": [(3, group_auction_seller_user.id)]})
