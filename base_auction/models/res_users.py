# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class Users(models.Model):
    _inherit = "res.users"

    is_auction_user = fields.Boolean(
        compute="_compute_is_auction_user", inverse="_inverse_is_auction_user"
    )

    def _compute_is_auction_user(self):
        for user in self:
            user.is_auction_user = False
            if user.has_group("base_auction.group_auction_user"):
                user.is_auction_user = True

    def _inverse_is_auction_user(self):
        group_auction_user = self.env.ref("base_auction.group_auction_user")
        for user in self:
            if user.is_auction_user:
                user.write({"groups_id": [(4, group_auction_user.id)]})
            else:
                user.write({"groups_id": [(3, group_auction_user.id)]})
