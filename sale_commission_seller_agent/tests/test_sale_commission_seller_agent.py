# Copyright 2023 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.tests import Form
from odoo.tests.common import TransactionCase


class TestSaleCommissionSellerAgent(TransactionCase):
    def setUp(self):
        super(TestSaleCommissionSellerAgent, self).setUp()
        self.sale_order_model = self.env["sale.order"]
        self.partner = self.env.ref("base.res_partner_2")
        self.agent = self.env.ref("commission.res_partner_pritesh_sale_agent")
        self.agent.write({"is_seller_partner": True})
        self.seller_product = self.env["product.product"].create(
            {
                "name": "Test seller product",
                "list_price": 5,
                "seller_id": self.agent.id,
            }
        )

    def _create_sale_order(self):
        order_form = Form(self.sale_order_model)
        order_form.partner_id = self.partner
        with order_form.order_line.new() as line_form:
            line_form.product_id = self.seller_product
        order = order_form.save()
        return order

    def test_sale_commission_seller_agent(self):
        order = self._create_sale_order()
        agent = order.order_line.mapped("agent_ids.agent_id")
        self.assertEqual(self.agent, agent)
