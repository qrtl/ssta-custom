# Copyright 2023 Quartile Limited (https://www.quartile.co)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    event_ids = fields.Many2many(
        comodel_name="event.event", compute="_compute_event_ids"
    )
    tax_totals_json_signed = fields.Char(
        string="Invoice Totals JSON Signed",
        compute="_compute_tax_totals_json_signed",
    )

    @api.depends("settlement_ids", "settlement_ids.event_ids")
    def _compute_event_ids(self):
        for move in self:
            move.event_ids = move.settlement_ids.mapped("event_ids")

    # TODO: consider cutting this out to a separate module
    @api.depends("tax_totals_json")
    def _compute_tax_totals_json_signed(self):
        """Computes the tax totals string to be displayed in views/reports, with minus
        symbol ("-") addition to the amounts for refunds.
        """
        super()._compute_tax_totals_json()
        for move in self:
            if move.move_type not in ("out_refund", "in_refund"):
                move.tax_totals_json_signed = move.tax_totals_json
                continue
            # '\u00a0' is no-break space which only appear in between currency symbol
            # and amount in the tax_totals_json string.
            move.tax_totals_json_signed = move.tax_totals_json.replace(
                r"\u00a0", r"\u00a0-"
            )
        return
