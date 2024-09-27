# Copyright 2024 Quartile (https://www.quartile.co)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def button_draft(self):
        products = self.order_line.mapped("product_id")
        products.write({"active": True})
        products.mapped("product_tmpl_id").write({"active": True})
        return super().button_draft()

    def button_cancel(self):
        products = self.order_line.mapped("product_id")
        products.write({"active": False})
        products.mapped("product_tmpl_id").write({"active": False})
        return super().button_cancel()
