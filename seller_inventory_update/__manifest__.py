# Copyright 2023 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Seller Inventory Update",
    "category": "Stock",
    "version": "15.0.1.0.0",
    "author": "Quartile Limited",
    "website": "https://www.quartile.co",
    "license": "AGPL-3",
    "depends": ["stock", "auction_seller"],
    "data": [
        "security/ir.model.access.csv",
        "wizard/seller_inventory_update_views.xml",
    ],
    "installable": True,
}
