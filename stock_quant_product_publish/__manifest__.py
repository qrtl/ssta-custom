# Copyright 2017-2018 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Stock Quant Product Publish",
    "version": "15.0.1.0.0",
    "author": "Quartile Limited",
    "website": "https://www.quartile.co",
    "category": "Stock",
    "license": "AGPL-3",
    "depends": [
        "product_yahoo_auction_sst",
    ],
    "data": [
        "security/ir.model.access.csv",
        "wizards/stock_quant_product_publish_wizard.xml",
    ],
    "installable": True,
}
