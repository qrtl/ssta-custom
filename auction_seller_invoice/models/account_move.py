# Copyright 2022 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    amount_untaxed_signed_positive = fields.Monetary(
        string="Untaxed Amount Signed",
        store=True,
        readonly=True,
        compute="_compute_amount_positive",
        currency_field="company_currency_id",
    )
    amount_tax_signed_positive = fields.Monetary(
        string="Tax Signed",
        store=True,
        readonly=True,
        compute="_compute_amount_positive",
        currency_field="company_currency_id",
    )
    amount_total_signed_positive = fields.Monetary(
        string="Total Signed",
        store=True,
        readonly=True,
        compute="_compute_amount_positive",
        currency_field="company_currency_id",
    )

    @api.depends("amount_untaxed_signed", "amount_tax_signed", "amount_total_signed")
    def _compute_amount_positive(self):
        for move in self:
            if move.move_type == "in_invoice" or "in_refund":
                move.amount_untaxed_signed_positive = move.amount_untaxed_signed * -1
                move.amount_tax_signed_positive = move.amount_tax_signed * -1
                move.amount_total_signed_positive = move.amount_total_signed * -1
            else:
                move.amount_untaxed_signed_positive = move.amount_untaxed_signed
                move.amount_tax_signed_positive = move.amount_tax_signed
                move.amount_total_signed_positive = move.amount_total_signed
