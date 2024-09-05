# Copyright 2024 Quartile Limited (https://www.quartile.co)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SettlementReportType(models.Model):
    _name = "settlement.report.type"
    _description = "Settlement Report Type"

    name = fields.Char()
    company_id = fields.Many2one("res.company", required=True)
    seller_settlement_report_title = fields.Char(
        help="Title to show on the seller settlement report."
    )
    case_number = fields.Boolean(
        help="Show case number on the seller settlement report.", default=True
    )
    company_address = fields.Text(
        help="Address to show on the seller settlement report."
    )
    seller_settlement_report_debit_comment = fields.Text(
        help="Comment to show below the total amount on the seller settlement report "
        "when the balance is positive."
    )
    seller_settlement_report_credit_comment = fields.Text(
        help="Comment to show below the total amount on the seller settlement report "
        "when the balance is negative."
    )
    seller_settlement_report_settlement_comment = fields.Text(
        help="Comment to show below the total amount of Sold Items on the seller "
        "settlement report "
    )
    active = fields.Boolean(default=True)
