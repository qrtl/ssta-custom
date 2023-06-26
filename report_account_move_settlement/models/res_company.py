# Copyright 2023 Quartile Limited (https://www.quartile.co)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class Company(models.Model):
    _inherit = "res.company"

    seller_settlement_report_title = fields.Char(
        help="Title to show on the seller settlement report."
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
