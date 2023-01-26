from odoo.tests.common import TransactionCase


class TestSaleOrderLineCaseNumber(TransactionCase):
    def setUp(self):
        super(TestSaleOrderLineCaseNumber, self).setUp()
        self.product1 = self.env["product.template"].create(
            {
                "name": "Product1",
                "list_price": 100.00,
                "default_code": "Test",
                "case_number": "123",
            }
        )
        self.product2 = self.env["product.template"].create(
            {
                "name": "Product2",
                "list_price": 100.00,
                "default_code": "Test2",
                "case_number": "123",
            }
        )
        self.partner = self.env["res.partner"].create({"name": "Customer - test"})

    def _create_sale_order(self, product):
        sale_order = self.env["sale.order"].create(
            {
                "partner_id": self.partner.id,
                "order_line": [
                    (
                        0,
                        0,
                        {
                            "name": product.name,
                            "product_id": product.product_variant_ids.id,
                            "product_uom_qty": 1,
                            "price_unit": 100.00,
                        },
                    )
                ],
            }
        )
        return sale_order

    def test_sale_order_line_case_number(self):
        order = self._create_sale_order(self.product1)
        order_line = order.order_line
        order_line.product_id_change()
        self.assertEqual(order_line.name, "[Test][123] Product1")

        order = self._create_sale_order(self.product2)
        order_line = order.order_line
        order_line.product_id_change()
        self.assertEqual(order_line.name, "[Test2][123] Product2")
