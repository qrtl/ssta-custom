# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import _, api, fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    request_medium_id = fields.Many2one("request.medium", "Request Medium")
    purchase_category_id = fields.Many2one("purchase.category", "Purchase Category",)
    shop_id = fields.Many2one("stock.warehouse", "Shop")
    