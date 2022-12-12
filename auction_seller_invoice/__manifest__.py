# Copyright 2022 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Auction Seller Invoice",
    "category": "Auction",
    "version": "15.0.1.0.0",
    "author": "Quartile Limited",
    "website": "https://www.quartile.co",
    "license": "AGPL-3",
    "depends": [
        "account",
        "account_commission",
        "auction_seller",
    ],
    "data": [
        "security/ir.model.access.csv",
        "security/auction_security.xml",
        "data/seller_board_data.xml",
        "views/auction_item_invoice_views.xml",
        "views/seller_board_views.xml",
    ],
    "installable": True,
}
