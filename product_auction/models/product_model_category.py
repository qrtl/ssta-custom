# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class ProductModelCategory(models.Model):
    _name = "product.model.category"
    _description = "Product Model Category"
    _order = "sequence"

    name = fields.Char()
    active = fields.Boolean(default=True)
    sequence = fields.Integer(default=16, required=True)

    _sql_constraints = [("name", "unique(name)", "This category is already exist.")]
