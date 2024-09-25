# Copyright 2017 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Stock Quant List View",
    "version": "15.0.1.0.0",
    "author": "Quartile Limited",
    "website": "https://www.quartile.co",
    "category": "Stock",
    "license": "AGPL-3",
    "depends": [
        "product_yahoo_auction_sst",  # yahoo_product_state_id
        "stock_sales_channel",  # sales_channel_id
        "product_seller",  # seller_id
    ],
    "data": ["views/stock_quant_views.xml"],
    "installable": True,
}
