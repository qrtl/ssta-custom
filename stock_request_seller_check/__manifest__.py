# Copyright 2023 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Stock Request Seller Check",
    "category": "Stock",
    "version": "15.0.1.0.0",
    "author": "Quartile Limited",
    "website": "https://www.quartile.co",
    "license": "AGPL-3",
    "depends": ["stock_request", "auction_seller"],
    "data": [
        "views/stock_request_order_views.xml",
        "views/stock_request_views.xml",
    ],
    "installable": True,
}
