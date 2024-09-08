# Copyright 2022 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields

from odoo.addons.account_commission.tests.test_account_commission import (
    TestAccountCommission,
)


class TestAccountCommissionSalesFee(TestAccountCommission):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.sales_fee_product_id = cls.env["product.product"].create(
            {"name": "Sales fee test product", "type": "service", "list_price": 1}
        )

    def test_account_commission_sales_fee(self):
        agent = self.env.ref("commission.res_partner_pritesh_sale_agent")
        commission = self.commission_section_paid
        commission.write(
            {
                "calculate_sales_fee": True,
                "sales_fee_product_id": self.sales_fee_product_id,
            }
        )
        settlement = self._check_invoice_thru_settle(
            agent,
            commission,
            1,
            0,
        )
        invoice = settlement.invoice_id
        products = invoice.invoice_line_ids.mapped("product_id")
        self.assertIn(self.sales_fee_product_id, products)
        sales_fee_line = invoice.invoice_line_ids.filtered(
            lambda line: line.product_id.id == self.sales_fee_product_id.id
        )
        self.assertEqual(abs(sales_fee_line.quantity), 1.0)

    def test_multiple_account_commission_sales_fee(self):
        agent = self.agent_monthly
        commission = self.commission_net_invoice
        commission.write(
            {
                "calculate_sales_fee": True,
                "sales_fee_product_id": self.sales_fee_product_id,
            }
        )
        today = fields.Date.today()
        invoice_1 = self._create_invoice(agent, commission, today)
        invoice_1.action_post()
        invoice_2 = self._create_invoice(agent, commission, today)
        invoice_2.action_post()
        self._settle_agent_invoice(agent, 1)
        settlements = self.settle_model.search(
            [
                ("agent_id", "=", agent.id),
                ("state", "=", "settled"),
            ]
        )
        settlements.make_invoices(self.journal, self.commission_product, grouped=True)
        invoice = settlements.invoice_id
        products = invoice.invoice_line_ids.mapped("product_id")
        self.assertIn(self.sales_fee_product_id, products)
        sales_fee_line = invoice.invoice_line_ids.filtered(
            lambda line: line.product_id.id == self.sales_fee_product_id.id
        )
        self.assertEqual(abs(sales_fee_line.quantity), 2.0)
