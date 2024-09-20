# Copyright 2024 Quartile
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class StockQuant(models.Model):
    _inherit = "stock.quant"

    seller_id = fields.Many2one(related="product_id.seller_id", store=True)
