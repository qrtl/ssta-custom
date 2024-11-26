# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.tools import ImageProcess

IMAGE_TYPES = ["image/png", "image/jpeg", "image/bmp", "image/tiff"]


class IrAttachment(models.Model):
    _inherit = "ir.attachment"

    resize_done = fields.Boolean()

    # This function was for only purpose of updating existing old datas
    # Resizing the new image will be handled by attachment_resize_image
    @api.model
    def _resize_image(self, datas):
        ICP = self.env["ir.config_parameter"].sudo().get_param
        # Use 1025 instead of 1024 to enable the zoom feature.
        # Define a static value instead of modifying the system parameter
        # 'base.image_autoresize_max_px' to avoid
        # affecting attachment resize.
        nw, nh = (1025, 1025)
        quality = int(ICP("base.image_autoresize_quality", 80))
        img = ImageProcess(datas, verify_resolution=False)
        w, h = img.image.size
        if w > nw or h > nh:
            # Use odoo standard resize
            img = img.resize(nw, nh)
            return img.image_base64(quality=quality)
        return datas

    @api.model
    def _cron_resize_attachment_image(self, limit):
        attachments = self.sudo().search(
            [
                ("mimetype", "in", IMAGE_TYPES),
                ("res_model", "in", ["product.template", "product.product"]),
                ("resize_done", "=", False),
                ("res_field", "=", False),
            ],
            limit=limit,
        )
        for attachment in attachments:
            attachment.datas = self._resize_image(attachment.datas)
            attachments.resize_done = True

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
                vals = {}
                # assignment for pt and p
                if attachment.res_model == "product.template":
                    pt = self.env["product.template"].browse(attachment.res_id)
                    vals = {
                        "name": attachment.name,
                        "image_1920": attachment.datas,
                        "product_tmpl_id": pt.id,
                    }
                if attachment.res_model == "product.product":
                    p = self.env["product.product"].browse(attachment.res_id)
                    vals = {
                        "name": attachment.name,
                        "image_1920": attachment.datas,
                        "product_variant_id": p.id,
                    }
                self.env["product.image"].sudo().create(vals)
        return attachments
