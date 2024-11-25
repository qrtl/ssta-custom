# Copyright 2024 Quartile
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ProductImage(models.Model):
    _inherit = "product.image"

    resize_done = fields.Boolean()

    @api.model
    def _cron_resize_product_image(self, limit):
        images = self.sudo().search(
            [("can_image_1024_be_zoomed", "=", True), ("resize_done", "=", False)],
            limit=limit,
        )
        for image in images:
            image.image_1920 = self.env["ir.attachment"]._resize_image(image.image_1920)
            image.resize_done = True
