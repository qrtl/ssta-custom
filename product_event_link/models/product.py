# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class Product(models.Model):
    _inherit = "product.product"

    event_ids = fields.Many2many(
        "event.event", compute="_compute_product_event_ids", string="Events", store=True
    )

    def _compute_product_event_ids(self):
        for product in self:
            product.event_ids = False
