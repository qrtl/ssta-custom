# Copyright 2024 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    def _post(self, soft=True):
        moves = self.filtered(
            lambda move: not move.invoice_date and move.move_type == "in_invoice"
        )
        if moves:
            moves.write({"invoice_date": fields.Date.context_today(self)})
        return super()._post(soft)
