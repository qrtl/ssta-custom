# Copyright 2023 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    amount_total_delivered = fields.Monetary(
        string="Total Delivered Amount",
        store=True,
        compute="_compute_amount_delivered",
    )
    amount_total_delivered_signed = fields.Monetary(
        string="Total Delivered Amount (+/-)",
        store=True,
        compute="_compute_amount_delivered",
    )
    delivery_done = fields.Boolean(compute="_compute_amount_delivered", store=True)

    @api.depends(
        "invoice_line_ids.is_delivered",
        "invoice_line_ids.delivered_amount",
        "move_type",
    )
    def _compute_amount_delivered(self):
        for move in self:
            if move.move_type not in ["out_invoice", "out_refund"]:
                continue
            sign = -1 if move.move_type == "out_refund" else 1
            move.amount_total_delivered = sum(
                move.invoice_line_ids.mapped("delivered_amount")
            )
            move.amount_total_delivered_signed = move.amount_total_delivered * sign
            if move.amount_total_delivered == move.amount_total:
                move.delivery_done = True
