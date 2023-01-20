# Copyright 2023 Quartile Limited (https://www.quartile.co)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

import re

from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    event_ids = fields.Many2many(
        comodel_name="event.event", compute="_compute_event_ids"
    )
    tax_totals_json_negative = fields.Char(
        string="Invoice Totals JSON Negative",
        compute="_compute_tax_totals_json_negative",
        readonly=False,
        help="Edit Tax amounts if you encounter rounding issues.",
    )

    @api.depends("settlement_ids", "settlement_ids.event_ids")
    def _compute_event_ids(self):
        for move in self:
            move.event_ids = move.settlement_ids.mapped("event_ids")

    # Method to display negative numbers for tax_totals_json
    # that only displays positive numbers.
    # Because to use negative numbers in custom reports.
    @api.depends("tax_totals_json")
    def _compute_tax_totals_json_negative(self):
        super()._compute_tax_totals_json()
        for move in self:
            name = move.tax_totals_json
            neg_name = re.sub("u00a0", "u00a0-", name)
            move.tax_totals_json_negative = neg_name
        return
