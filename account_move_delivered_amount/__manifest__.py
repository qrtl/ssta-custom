# Copyright 2023 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Account Move Delivered Amount",
    "version": "15.0.1.0.0",
    "author": "Quartile Limited",
    "website": "https://www.quartile.co",
    "category": "Accounting",
    "license": "AGPL-3",
    "depends": ["sale_stock"],
    "data": ["views/account_move_views.xml"],
    "pre_init_hook": "pre_init_hook",
    "installable": True,
}
