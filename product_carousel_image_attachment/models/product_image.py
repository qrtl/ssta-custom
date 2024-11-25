# Copyright 2024 Quartile
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class ProductImage(models.Model):
    _inherit = "product.image"

    @api.model
    def _cron_resize_product_image(self, limit):
        images = self.sudo().search([], limit=limit)
        for image in images:
            image.image_1920 = self.env["ir.attachment"]._resize_image(image.image_1920)
        if len(images) == limit:
            self.env.ref(
                "product_carousel_image_attachment.resize_product_image"
            )._trigger()
