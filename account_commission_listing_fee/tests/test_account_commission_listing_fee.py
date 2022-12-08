from odoo.addons.account_commission.tests.test_account_commission import (
    TestAccountCommission,
)


class TestAccountCommissionListingFee(TestAccountCommission):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.listing_fee_product = cls.env["product.product"].create(
            {"name": "Listing fee test product", "type": "service", "list_price": 1}
        )

    # This test is only for testing listing_fee_product in settlement bill or not.
    # Need to add tests in auction_event module for adding seller_id and event_ids in prdouct
    # and can check quantity of listing_fee_product_id and number of items of settlement.
    def test_account_commission_listing_fee(self):
        agent = self.env.ref("commission.res_partner_pritesh_sale_agent")
        commission = self.commission_section_paid
        commission.write({"calculate_listing_fee": True})
        agent.write(
            {
                "commission_id": commission.id,
                "listing_fee_product_id": self.listing_fee_product.id,
            }
        )
        settlement = self._check_invoice_thru_settle(
            agent,
            commission,
            1,
            0,
        )
        invoice = settlement.invoice_id
        product_ids = invoice.mapped("invoice_line_ids.product_id").ids
        self.assertIn(self.listing_fee_product.id, product_ids)
