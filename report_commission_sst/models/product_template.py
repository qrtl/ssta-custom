# Copyright 2023 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    settle_product = fields.Boolean(help="If checked, this product is" 
    "not displyed in settlement report" )
