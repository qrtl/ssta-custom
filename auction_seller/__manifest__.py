# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
{
    "name": "Auction Seller",
    "category": "Auction",
    "version": "15.0.1.0.0",
    "author": "Quartile Limited",
    "website": "https://www.quartile.co",
    "license": "LGPL-3",
    "depends": ["portal"],
    "data": [
        "security/auction_seller_security.xml",
        "security/ir.model.access.csv",
        "data/menuitem_data.xml",
        "views/editor.xml",
        "views/res_users_views.xml",
    ],
    "installable": True,
}
