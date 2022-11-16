# Copyright 2022 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    agent_ids = fields.One2many(compute="_compute_agent_ids_by_product")

    @api.depends("product_id")
    def _compute_agent_ids_by_product(self):
        for record in self:
            if record.commission_free:
                continue
            # propose the seller of the product in agent line
            if record.product_id.seller_id and record.product_id.seller_id.agent:
                record.agent_ids = [
                    (0, 0, record._prepare_agent_vals(record.product_id.seller_id))
                ]
