# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
{
    "name": "Auction Seller",
    "category": "Auction",
    "version": "15.0.1.0.0",
    "author": "Quartile Limited",
    "website": "https://www.quartile.co",
    "license": "LGPL-3",
    "depends": ["event", "product_auction", "product_seller"],
    "data": [
        "security/auction_security.xml",
        "security/ir.model.access.csv",
        "views/product_template_views.xml",
        "views/seller_board_views.xml",
        "views/res_users_views.xml",
        "data/menuitem_data.xml",
        "data/seller_board_data.xml",
    ],
    "installable": True,
}
