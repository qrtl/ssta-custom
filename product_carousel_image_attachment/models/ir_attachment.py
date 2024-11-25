# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models
from odoo.tools import ImageProcess

IMAGE_TYPES = ["image/png", "image/jpeg", "image/bmp", "image/gif"]


class IrAttachment(models.Model):
    _inherit = "ir.attachment"

    def _resize_image(self, datas):
        ICP = self.env["ir.config_parameter"].sudo().get_param
        quality = int(ICP("base.image_autoresize_quality", 80))
        # Use 1025 instead of 1024 to enable the zoom feature
        max_resolution = (1025, 1025)
        img = ImageProcess(datas, verify_resolution=False)
        w, h = img.image.size
        nw, nh = map(int, max_resolution.split("x"))
        if w > nw or h > nh:
            img = img.resize(nw, nh)  # Resize the image
            return img.image_base64(
                quality=quality
            )  # Return the resized image as base64
        return datas

    @api.model_create_multi
    def create(self, vals_list):
        attachments = super(IrAttachment, self).create(vals_list)
        for attachment in attachments:
            if (
                attachment.mimetype in IMAGE_TYPES
                and attachment.res_model
                in [
                    "product.template",
                    "product.product",
                ]
                and not attachment.res_field
            ):
                resized_image = self._resize_image(attachment.datas)
                vals = {}
                # assignment for pt and p
                if attachment.res_model == "product.template":
                    pt = self.env["product.template"].browse(attachment.res_id)
                    vals = {
                        "name": attachment.name,
                        "image_1920": resized_image,
                        "product_tmpl_id": pt.id,
                    }
                if attachment.res_model == "product.product":
                    p = self.env["product.product"].browse(attachment.res_id)
                    vals = {
                        "name": attachment.name,
                        "image_1920": resized_image,
                        "product_variant_id": p.id,
                    }
                self.env["product.image"].sudo().create(vals)
        return attachments
