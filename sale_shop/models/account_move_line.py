# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    @api.model_create_multi
    def create(self, vals_list):
        res = super().create(vals_list)
        for rec in res:
            if rec.sale_line_ids and rec.sale_line_ids[0].order_id.warehouse_id:
                rec.move_id.shop_id = rec.sale_line_ids[0].order_id.warehouse_id.id
        return res
