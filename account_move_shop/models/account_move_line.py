# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    shop_id = fields.Many2one(
        related="move_id.shop_id",
        string="Shop",
        readonly=True,
    )
