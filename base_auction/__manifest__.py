# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
{
    "name": "Base Auction",
    "category": "Auction",
    "version": "15.0.1.0.0",
    "author": "Quartile Limited",
    "website": "https://www.quartile.co",
    "license": "LGPL-3",
    "depends": ["portal"],
    "data": [
        "security/auction_security.xml",
        "security/ir.model.access.csv",
        "views/base_auction_views.xml",
        "views/editor.xml",
        "views/res_users_views.xml",
    ],
    "installable": True,
}
