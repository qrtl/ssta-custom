# Copyright 2022 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class CommissionSettlement(models.Model):
    _inherit = "commission.settlement"

    def _prepare_sales_fee_product(self, commission):
        return {
            "product_id": commission.sales_fee_product_id.id,
            "quantity": len(
                self.line_ids.filtered(lambda line: line.commission_id == commission)
            ),
            "price_unit": commission.sales_fee_product_id.list_price * -1,
            "tax_ids": [(6, 0, commission.sales_fee_product_id.supplier_taxes_id.ids)],
        }

    def _prepare_invoice(self, journal, product, date=False):
        res = super()._prepare_invoice(journal, product, date)
        if res["invoice_line_ids"]:
            commissions = self.mapped("line_ids.commission_id")
            for commission in commissions:
                if commission.calculate_sales_fee:
                    res["invoice_line_ids"].append(
                        (0, 0, self._prepare_sales_fee_product(commission))
                    )
            # Clear line_ids because invoice_line_ids will be cleared if line_ids
            # is available in _move_autocomplete_invoice_lines_create() that is
            # called in create method.
            if "line_ids" in res:
                res.pop("line_ids", None)
        return res
