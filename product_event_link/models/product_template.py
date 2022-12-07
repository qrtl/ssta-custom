# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    event_ids = fields.Many2many(
        "event.event", compute="_compute_event_ids", string="Events", store=True
    )

    @api.depends("product_variant_ids.event_ids")
    def _compute_event_ids(self):
        for template in self:
            variants = template.product_variant_ids
            template.event_ids = variants.mapped("event_ids")
