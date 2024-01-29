# Copyright 2019 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _name = "purchase.order"
    _inherit = ["purchase.order", "zip.code.search.mixin"]

    country_id = fields.Many2one(
        "res.country", string="Country", default=lambda self: self.env.ref("base.jp")
    )
    state_id = fields.Many2one("res.country.state", string="Prefecture")
    city = fields.Char()
    street = fields.Char()
    street2 = fields.Char()
    zip = fields.Char(
        related="partner_id.zip",
        string="Post Code (Supplier)",
        store=True,
        readonly=True,
    )

    @api.onchange("partner_id")
    def _onchange_partner_id(self):
        if self.partner_id and not self.zipcode and not self.street:
            self.state_id = self.partner_id.state_id
            self.city = self.partner_id.city
            self.street = self.partner_id.street
            self.street2 = self.partner_id.street2

    def write(self, vals):
        res = super(PurchaseOrder, self).write(vals)
        for order in self:
            if (
                not self.is_default_partner(order.partner_id.id)
                and order.zipcode
                and not order.partner_id.zip
            ):
                order.partner_id.zip = order.zipcode
                order.partner_id.state_id = order.state_id
                order.partner_id.city = order.city
                order.partner_id.street = order.street
                order.partner_id.street2 = order.street2
        return res

    @api.model
    def create(self, vals):
        res = super(PurchaseOrder, self).create(vals)
        if (
            not self.is_default_partner(res.partner_id.id)
            and res.zipcode
            and not res.partner_id.zip
        ):
            res.partner_id.zip = res.zipcode
            res.partner_id.state_id = res.state_id
            res.partner_id.city = res.city
            res.partner_id.street = res.street
            res.partner_id.street2 = res.street2
        return res
