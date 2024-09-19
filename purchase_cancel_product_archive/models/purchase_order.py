# Copyright 2024 Quartile (https://www.quartile.co)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def write(self, vals):
        if not vals.get("state"):
            return super().write(vals)
        for rec in self:
            products = rec.order_line.mapped("product_id")
            if rec.state == "cancel":
                products.write({"active": True})
                products.mapped("product_tmpl_id").write({"active": True})
            elif vals["state"] == "cancel":
                products.write({"active": False})
                products.mapped("product_tmpl_id").write({"active": False})
        return super().write(vals)
