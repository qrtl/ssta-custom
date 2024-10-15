# Copyright 2024 Quartile
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class CommissionSettlement(models.Model):
    _inherit = "commission.settlement"

    commission_ids = fields.Many2many(
        comodel_name="commission", compute="_compute_commission_ids", store=True
    )

    @api.depends("line_ids.commission_id")
    def _compute_commission_ids(self):
        for rec in self:
            rec.commission_ids = rec.line_ids.mapped("commission_id")
