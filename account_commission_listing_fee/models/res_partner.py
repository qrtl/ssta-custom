# Copyright 2022 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    listing_fee_product_id = fields.Many2one(
        comodel_name="product.product", domain="[('type', '=', 'service')]"
    )
