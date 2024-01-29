# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    @api.model
    def _get_date_planned(self, seller, po=False):
        if self.order_id.date_planned:
            return self.order_id.date_planned
        return super()._get_date_planned(seller, po)

    def open_product_record(self):
        form_id = self.env.ref("product.product_normal_form_view")
        return {
            "type": "ir.actions.act_window",
            "res_model": "product.product",
            "res_id": self.product_id.id,
            "view_type": "form",
            "view_mode": "form",
            "view_id": form_id.id,
            "context": {},
            "target": "current",
        }
