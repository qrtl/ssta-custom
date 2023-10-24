# Copyright 2020 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo.tests import common


class TestProduct(common.TransactionCase):
    @classmethod
    def setUpClass(cls):
        super(TestProduct, cls).setUpClass()

        stock_location = cls.env.ref("stock.stock_location_stock")
        product_product = cls.env["product.product"]
        stock_quant = cls.env["stock.quant"]

        cls.product_01 = product_product.create(
            {"name": "Test Product 01", "type": "product"}
        )
        cls.product_02 = product_product.create(
            {"name": "Test Product 02", "type": "product"}
        )
        cls.product_03 = product_product.create(
            {"name": "Test Product 03", "type": "product"}
        )

        # Create stock for products
        stock_quant._update_available_quantity(cls.product_01, stock_location, 100.0)
        stock_quant._update_available_quantity(cls.product_02, stock_location, 100.0)

        cls.partner = cls.env["res.partner"].create({"name": "Test Partner"})

    def test_01_compute_virtual_available(self):
        sale_order = self.env["sale.order"]

        def _create_line(product, qty, order):
            return self.env["sale.order.line"].create(
                {
                    "product_id": product.id,
                    "price_unit": 10.00,
                    "product_uom": product.uom_id.id,
                    "product_uom_qty": qty,
                    "order_id": order.id,
                }
            )

        # Create an order with 'draft' state
        sale_order_01 = sale_order.create({"partner_id": self.partner.id})
        _create_line(self.product_01, 20.0, sale_order_01)
        _create_line(self.product_02, 30.0, sale_order_01)

        # Create an order with 'draft' state
        sale_order_02 = sale_order.create({"partner_id": self.partner.id})
        _create_line(self.product_01, 15.0, sale_order_02)

        # Create an order with 'sent' state
        sale_order_03 = sale_order.create({"partner_id": self.partner.id})
        _create_line(self.product_02, 10.0, sale_order_03)

        # Change state directly to sent
        sale_order_03.state = "sent"

        self.assertEqual(self.product_01.draft_sale_qty, 35.0)
        self.assertEqual(self.product_01.sent_sale_qty, 0.0)
        self.assertEqual(self.product_02.draft_sale_qty, 30.0)
        self.assertEqual(self.product_02.sent_sale_qty, 10.0)

        # Check the result at product variant level
        self.assertEqual(self.product_01.virtual_available, 65.0)
        self.assertEqual(self.product_02.virtual_available, 60.0)

        # Check the result at product template level
        self.assertEqual(
            self.product_01.product_tmpl_id.virtual_available,
            65.0,
        )
        self.assertEqual(
            self.product_02.product_tmpl_id.virtual_available,
            60.0,
        )
