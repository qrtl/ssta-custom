# Copyright 2017 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProductPrepState(models.Model):
    _name = "product.prep.state"
    _description = "Product Preparation State"

    name = fields.Char(require=True)
