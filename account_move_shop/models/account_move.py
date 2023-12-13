# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    shop_id = fields.Many2one(
        "stock.warehouse",
        string="Shop",
        readonly=True,
        states={"draft": [("readonly", False)]},
    )
