# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class ProductModel(models.Model):
    _name = "product.model"
    _description = "Product Model"
    _order = "sequence"

    name = fields.Char()
    active = fields.Boolean(default=True)
    sequence = fields.Integer(default=16, required=True)
    category_id = fields.Many2one(
        comodel_name="product.model.category",
        string="Product Model Category",
        required=True,
    )

    _sql_constraints = [("name", "unique(name)", "Name must be unique!")]
