# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
{
    "name": "Auction Seller Product",
    "category": "Auction",
    "version": "15.0.1.0.0",
    "author": "Quartile Limited",
    "website": "https://www.quartile.co",
    "license": "LGPL-3",
    "depends": ["product", "base_auction"],
    "data": [
        "security/ir.model.access.csv",
        "security/auction_seller_product_security.xml"
        # "views/product_product_views.xml",
        # "views/product_template_views.xml",
    ],
    "installable": True,
}
