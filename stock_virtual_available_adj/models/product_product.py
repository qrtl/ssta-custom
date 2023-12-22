# Copyright 2018 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    draft_sale_qty = fields.Float(
        "Sale Quantity (Draft)",
        compute="_compute_sale_quantities",
        help="Total quantity of the product in draft sales order(s)",
    )
    sent_sale_qty = fields.Float(
        "Sale Quantity (Sent)",
        compute="_compute_sale_quantities",
        help="Total quantity of the product in sent sales order(s)",
    )

    def _compute_sale_quantities(self):
        for product in self:
            sale_lines = self.env["sale.order.line"].search(
                [("product_id", "=", product.id), ("state", "in", ("sent", "draft"))]
            )
            product.draft_sale_qty = sum(
                sale_lines.filtered(lambda p: p.state == "draft").mapped(
                    "product_uom_qty"
                )
            )
            product.sent_sale_qty = sum(
                sale_lines.filtered(lambda p: p.state == "sent").mapped(
                    "product_uom_qty"
                )
            )

    @api.depends("stock_move_ids.product_qty", "stock_move_ids.state")
    @api.depends_context(
        "lot_id",
        "owner_id",
        "package_id",
        "from_date",
        "to_date",
        "location",
        "warehouse",
    )
    def _compute_quantities(self):
        super()._compute_quantities()
        for product in self:
            product.virtual_available = (
                product.virtual_available
                - product.sent_sale_qty
                - product.draft_sale_qty
            )
        return
