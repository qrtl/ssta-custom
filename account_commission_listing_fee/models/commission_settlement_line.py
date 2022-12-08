# Copyright 2022 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SettlementLine(models.Model):
    _inherit = "commission.settlement.line"

    product_id = fields.Many2one(
        comodel_name="product.product",
        related="invoice_line_id.product_id",
        store=True,
    )
