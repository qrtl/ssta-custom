# Copyright 2017-2023 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    address = fields.Char()
    remark = fields.Text()
    date_planned = fields.Datetime(compute=False)
    sale_prediction_amount = fields.Monetary("Sales Prediction")

    def button_confirm(self):
        for order in self:
            if self.is_default_partner(order.partner_id.id):
                raise UserError(
                    _("Purchase order cannot be confirmed with default guest user.")
                )
            if not order.date_planned:
                order.date_planned = fields.Datetime.now()
                for order_line in order.order_line:
                    order_line.date_planned = order.date_planned
        return super(PurchaseOrder, self).button_confirm()

    def is_default_partner(self, partner_id):
        company = self.env.user.company_id
        return partner_id == company.purchase_default_partner_id.id

    @api.onchange("date_planned")
    def onchange_date_planned(self):
        if self.date_planned:
            for line in self.order_line:
                line.date_planned = self.date_planned
