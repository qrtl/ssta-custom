# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    supplier_phone = fields.Char(
        related="partner_id.phone",
        string="Supplier Phone",
        readonly=True,
        store=True,
    )
    supplier_mobile = fields.Char(
        related="partner_id.mobile",
        string="Supplier Mobile",
        readonly=True,
        store=True,
    )
