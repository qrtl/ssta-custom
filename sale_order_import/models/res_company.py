# Copyright 2023 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    def _picking_policy_selection(self):
        return self.env["sale.order"]._fields["picking_policy"].selection

    picking_policy = fields.Selection(
        _picking_policy_selection,
        string="Shipping Policy",
    )
    customer_invoice_journal_id = fields.Many2one(
        "account.journal",
        string="Customer Invoice Journal",
    )
    customer_payment_journal_id = fields.Many2one(
        "account.journal",
        string="Customer Payment Journal",
    )
