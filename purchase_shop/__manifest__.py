# Copyright 2017 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Purchase Shop",
    "version": "15.0.1.0.0",
    "author": "Quartile Limited",
    "website": "https://www.quartile.co",
    "category": "Purchase",
    "license": "AGPL-3",
    "depends": ["hr", "purchase_stock", "account_move_shop"],
    "data": [
        "views/hr_employee_views.xml",
        "views/purchase_order_views.xml",
        "views/product_template_views.xml",
    ],
    "installable": True,
}
