# Copyright 2022-2024 Quartile
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    is_seller_partner = fields.Boolean(
        help="If selected, the partner can be set as a seller in products."
    )
