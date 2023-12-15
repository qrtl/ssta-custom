# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models


class AccountMove(models.Model):
    _inherit = "account.move"

    @api.onchange("invoice_line_ids")
    def invoice_line_ids_onchange(self):
        if self.invoice_line_ids and not self.shop_id:
            for invoice_line_id in self.invoice_line_ids:
                if (
                    invoice_line_id.purchase_order_id
                    and invoice_line_id.purchase_order_id.shop_id
                ):
                    self.shop_id = invoice_line_id.purchase_order_id.shop_id.id
                    return

    @api.model_create_multi
    def create(self, vals_list):
        res = super().create(vals_list)
        for rec in res:
            rec.invoice_line_ids_onchange()
        return res
