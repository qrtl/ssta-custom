# Copyright 2024 Quartile (https://www.quartile.co)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class Product(models.Model):
    _inherit = "product.product"

    old_id = fields.Integer()
