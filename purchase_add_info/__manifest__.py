# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "Purchase Add Info",
    "version": "15.0.1.0.0",
    "author": "Quartile Limited",
    "website": "https://www.quartile.co",
    "category": "Purchase",
    "license": "LGPL-3",
    "depends": ["hr", "purchase"],
    "data": [
        "security/ir.model.access.csv",
        "data/menuitem_data.xml",
        "views/request_medium_views.xml",
        "views/purchase_category_views.xml",
        "views/purchase_order_views.xml",
    ],
    "installable": True,
}
