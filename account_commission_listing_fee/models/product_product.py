# Copyright 2022 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    settlement_id = fields.Many2one(
        comodel_name="commission.settlement", string="Settlement"
    )
