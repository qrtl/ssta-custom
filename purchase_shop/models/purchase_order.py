# Copyright 2017-2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    employee_id = fields.Many2one("hr.employee", "Received By")
    shop_id = fields.Many2one("stock.warehouse", "Shop")
    purchased_by_id = fields.Many2one("hr.employee", "Buyer")

    @api.onchange("purchased_by_id")
    def onchange_purchased_by_id(self):
        if (not self.shop_id and self.purchased_by_id) or (
            self.shop_id
            and self.purchased_by_id
            and self.purchased_by_id.shop_id != self.shop_id
        ):
            self.shop_id = self.purchased_by_id.shop_id

    @api.onchange("shop_id")
    def onchange_shop_id(self):
        ids = []
        if self.shop_id:
            # Update domain filter on delivery staff
            staffs = self.env["hr.employee"].search([("shop_id", "=", self.shop_id.id)])
            ids.append(("id", "in", staffs.ids))
            # Clear the delivery staff value
            if (
                self.purchased_by_id
                and self.purchased_by_id.shop_id
                and self.purchased_by_id.shop_id != self.shop_id
            ):
                self.purchased_by_id = False
            # Update picking_type_id
            picking_type_id = self.env["stock.picking.type"].search(
                [
                    ("code", "=", "incoming"),
                    ("warehouse_id", "=", self.shop_id.id),
                    (
                        "warehouse_id.company_id",
                        "in",
                        [
                            self.env.context.get(
                                "company_id", self.env.user.company_id.id
                            ),
                            False,
                        ],
                    ),
                ],
                limit=1,
            )
            if picking_type_id:
                self.picking_type_id = picking_type_id
        return {"domain": {"purchased_by_id": ids}}

    def write(self, vals):
        res = super().write(vals)
        if (
            "order_line" in vals
            or "shop_id" in vals
            or "purchased_by_id" in vals
            or "evaluated_by_id" in vals
        ):
            for order in self:
                products = order.order_line.mapped("product_id")
                products.write(
                    {
                        "shop_id": order.shop_id.id,
                        "purchased_by_id": order.purchased_by_id.id,
                        "evaluated_by_id": order.employee_id.id,
                    }
                )
        return res
