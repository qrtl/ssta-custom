# Copyright 2017-2018 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Products' Yahoo Auction information",
    "version": "15.0.1.0.0",
    "author": "Quartile Limited",
    "website": "https://www.quartile.co",
    "category": "Product",
    "license": "AGPL-3",
    "depends": ["product", "delivery"],
    "data": [
        "security/ir.model.access.csv",
        "data/delivery_carrier_data.xml",
        "data/delivery_carrier_size_data.xml",
        "data/yahoo_product_state.xml",
        "views/delivery_carrier_size_views.xml",
        "views/product_template_views.xml",
        "views/yahoo_product_state_views.xml",
    ],
    "installable": True,
}
