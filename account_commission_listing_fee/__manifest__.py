# Copyright 2022 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Account Commission listing Fee",
    "version": "15.0.1.0.0",
    "category": "Commission",
    "author": "Quartile Limited",
    "website": "https://www.quartile.co",
    "depends": ["account_commission", "product_event_link", "auction_seller"],
    "license": "AGPL-3",
    "data": [
        "views/commission_views.xml",
        "views/commission_settlement_views.xml",
        "views/res_partner_views.xml",
    ],
    "installable": True,
}
