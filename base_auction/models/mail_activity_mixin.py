# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class MailActivityMixin(models.AbstractModel):
    _inherit = "mail.activity.mixin"

    is_auction_user = fields.Boolean(
        compute="_compute_is_auction_user", inverse="_inverse_is_auction_user"
    )
    # Ading base_auction.group_auction_user to prevent access errors.
    # TODO: Check if this change is really valid.
    activity_ids = fields.One2many(
        groups="base.group_user,base_auction.group_auction_user"
    )
