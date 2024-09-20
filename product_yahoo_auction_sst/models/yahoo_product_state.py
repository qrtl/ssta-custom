# Copyright 2023 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class YahooProductState(models.Model):
    _name = "yahoo.product.state"

    # We assume that there is just a single (internal) quant per product;
    # the performance risk of `store=True` is minimal.
    name = fields.Char(
        string="Status",
        require=True,
    )
