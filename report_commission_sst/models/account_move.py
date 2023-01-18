# Copyright 2023 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models ,_
from odoo.exceptions import ValidationError

class AccountMove(models.Model):
    _inherit = "account.move"

    def action_print_commission_report(self):
        report_ref = "report_commission_sst.action_report_settlement_sst"
        settlement = self.settlement_ids.ids
        if not settlement:
            raise ValidationError(_("This record has no settlements"))
        return self.env.ref(report_ref).report_action([settlement])
