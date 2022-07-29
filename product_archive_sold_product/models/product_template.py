# Copyright 2022 Quartile Limited

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_sold = fields.Boolean(compute="_compute_is_sold", string="Sold", store=True
    )

    @api.depends("product_variant_ids.is_sold")
    def _compute_is_sold(self):
        for template in self:
            variants = template.product_variant_ids
            template.is_sold = variants.mapped("is_sold")
