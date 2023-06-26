# Copyright 2022 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class CommissionSettlement(models.Model):
    _inherit = "commission.settlement"

    event_ids = fields.Many2many(
        "event.event", compute="_compute_event_ids", string="Events", store=True
    )
    number_of_items = fields.Integer(compute="_compute_number_of_items", store=True)

    @api.depends("line_ids")
    def _compute_event_ids(self):
        for settlement in self:
            events = settlement.line_ids.product_id.event_ids
            settlement.event_ids = events

    @api.depends("event_ids", "agent_id")
    def _compute_number_of_items(self):
        for settlement in self:
            event_ids = settlement.event_ids.ids
            if not event_ids:
                settlement.number_of_items = 0
                continue
            products = (
                self.env["product.product"]
                .search(
                    [
                        ("seller_id", "=", settlement.agent_id.id),
                        "|",
                        ("settlement_id", "=", False),
                        ("settlement_id", "=", settlement.id),
                    ]
                )
                .filtered(
                    lambda x: x.event_ids
                    and (event for event in x.event_ids.ids if event in event_ids)
                )
            )
            for product in products:
                product.update({"settlement_id": settlement.id})
            settlement.number_of_items = len(products)

    def _prepare_listing_fee_product(self):
        return {
            "product_id": self.agent_id.listing_fee_product_id.id,
            "quantity": sum(settlement.number_of_items for settlement in self),
            "price_unit": self.agent_id.listing_fee_product_id.list_price * -1,
            "tax_ids": self.agent_id.listing_fee_product_id.supplier_taxes_id,
        }

    def _prepare_invoice(self, journal, product, date=False):
        res = super()._prepare_invoice(journal, product, date)
        if res["invoice_line_ids"]:
            commission = self.agent_id.commission_id
            if commission.calculate_listing_fee:
                res["invoice_line_ids"].append(
                    (0, 0, self._prepare_listing_fee_product())
                )
            # Clear line_ids because invoice_line_ids will be cleared if line_ids
            # is available in _move_autocomplete_invoice_lines_create() that is
            # called in create method.
            if "line_ids" in res:
                res.pop("line_ids", None)
        return res

    def action_cancel(self):
        products = self.env["product.product"].search([("settlement_id", "=", self.id)])
        products.write({"settlement_id": False})
        return super().action_cancel()
