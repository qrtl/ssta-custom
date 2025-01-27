# Copyright 2017-2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    title = fields.Char(compute="_compute_get_title", store=True)
    product_category = fields.Char()
    product_condition_comment = fields.Text()
    accessories = fields.Char()
    remark = fields.Text()
    staff_in_charge = fields.Many2one("res.users", domain="[('share', '=', False)]")
    staff_initial = fields.Char()
    auction_start_price = fields.Float(
        string="Auction Starting Price", digits="Product Price"
    )
    auction_buyout_price = fields.Float(digits="Product Price")
    product_condition = fields.Selection([("new", "New"), ("used", "Used")])
    carrier_id = fields.Many2one("delivery.carrier", string="Delivery Method")
    carrier_size_id = fields.Many2one("delivery.carrier.size", string="Delivery Size")
    deliver_prefecture = fields.Char(string="Delivery Prefecture")
    delivery_cites = fields.Char(string="Delivery Cities")
    stock_time = fields.Float()
    stock_date = fields.Date()
    yahoo_product_state_id = fields.Many2one(
        "yahoo.product.state",
        string="Yahoo Product State",
    )

    @api.onchange("carrier_id")
    def _onchange_carrier_id(self):
        domain = []
        self.carrier_size_id = False
        if self.carrier_id:
            carrier_sizes = self.env["delivery.carrier.size"].search(
                [("carrier_id", "=", self.carrier_id.id)]
            )
            domain.append(("id", "in", carrier_sizes.ids))
        return {"domain": {"carrier_size_id": domain}}

    @api.depends("default_code")
    def _compute_get_title(self):
        for pt in self:
            pt.title = pt.default_code
