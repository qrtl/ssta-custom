# Copyright 2022 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Add supplier phone and mobile in purchase",
    "version": "15.0.1.0.0",
    "author": "Quartile Limited",
    "website": "https://www.quartile.co",
    "category": "Purchase",
    "license": "AGPL-3",
    "depends": [
        "purchase_ext_sst",  # is_default_partner()
    ],
    "data": [
        "views/purchase_order_views.xml",
    ],
    "installable": True,
}
