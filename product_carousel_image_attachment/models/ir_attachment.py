# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import io
import logging

from PIL import Image

from odoo import api, fields, models
from odoo.tools import ImageProcess

_logger = logging.getLogger(__name__)

IMAGE_TYPES = ["image/png", "image/jpeg", "image/bmp", "image/tiff"]


class IrAttachment(models.Model):
    _inherit = "ir.attachment"

    resize_done = fields.Boolean()

    @api.model
    def _resize_image(self, datas, is_raw=False):
        ICP = self.env["ir.config_parameter"].sudo().get_param
        # Use 1025 instead of 1024 to enable the zoom feature.
        # Define a static value instead of modifying the system parameter
        # 'base.image_autoresize_max_px' to avoid
        # affecting attachment resize.
        max_width, max_height = 1025, 1025
        quality = int(ICP("base.image_autoresize_quality", 80))
        try:
            # Use odoo standard resize
            if is_raw:
                img = ImageProcess(False, verify_resolution=False)
                img.image = Image.open(io.BytesIO(datas))
                img.original_format = (img.image.format or "").upper()
            else:
                img = ImageProcess(datas, verify_resolution=False)
            width, height = img.image.size
            if width > max_width or height > max_height:
                img = img.resize(max_width, max_height)
                return (
                    img.image_quality(quality=quality)
                    if is_raw
                    else img.image_base64(quality=quality)
                )
        except Exception as e:
            _logger.warning(f"Failed to resize image: {e}")
            return datas
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
        # here we resize the image first to avoid bloating the filestore
        for values in vals_list:
            mimetype = values.get("mimetype") or self._compute_mimetype(values)
            if mimetype and mimetype.startswith("image/"):
                # Resize raw binary or Base64 data
                if "raw" in values and values["raw"]:
                    values["raw"] = self._resize_image(values["raw"], is_raw=True)
                elif "datas" in values and values["datas"]:
                    values["datas"] = self._resize_image(values["datas"], is_raw=False)
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
