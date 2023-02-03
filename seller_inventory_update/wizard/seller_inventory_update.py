# Copyright 2023 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class SellerInventoryUpdateWizard(models.TransientModel):
    _name = "seller.inventory.update.wizard"
    _description = "Seller Inventory Wizard"

    @api.model
    def _default_warehouse_id(self):
        return self.env.user._get_default_warehouse_id()

    company_id = fields.Many2one(
        "res.company",
        "Company",
        required=True,
        index=True,
        default=lambda self: self.env.company,
    )
    warehouse_id = fields.Many2one(
        "stock.warehouse",
        string="Warehouse",
        required=True,
        default=_default_warehouse_id,
        check_company=True,
    )

    def default_get(self, fields):
        context = dict(self._context or {})
        active_ids = context.get("active_ids", [])
        active_ids = context.get("active_ids", [])
        if context.get("active_model") == "product.template":
            products = (
                self.env["product.template"]
                .browse(active_ids)
                .mapped("product_variant_id")
            )
        else:
            products = self.env["product.product"].browse(active_ids)
        for product in products:
            if product.seller_id:
                continue
            raise UserError(_("You cannot select product that doesn't have seller."))
        return super().default_get(fields)

    def update_seller_inventory(self):
        context = dict(self._context or {})
        active_ids = context.get("active_ids", [])
        active_ids = context.get("active_ids", [])
        if context.get("active_model") == "product.template":
            products = (
                self.env["product.template"]
                .browse(active_ids)
                .mapped("product_variant_id")
            )
        else:
            products = self.env["product.product"].browse(active_ids)
        for product in products:
            self.env["stock.quant"].with_context(inventory_mode=True).create(
                {
                    "product_id": product.id,
                    "inventory_quantity": 1,
                    "location_id": self.warehouse_id.lot_stock_id.id,
                }
            ).action_apply_inventory()
