# Copyright 2024 Quartile
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class StockQuant(models.Model):
    _inherit = "stock.quant"

    # We assume that there is just a single (internal) quant per product;
    # the performance risk of `store=True` is minimal.
    seller_id = fields.Many2one(related="product_id.seller_id", store=True)
