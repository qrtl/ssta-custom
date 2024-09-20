# Copyright 2024 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class StockQuant(models.Model):
    _inherit = "stock.quant"

    yahoo_product_state_id = fields.Many2one(
        related="product_id.yahoo_product_state_id",
        string="Yahoo Product State",
        store=True,
    )
