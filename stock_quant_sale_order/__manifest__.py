# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Stock Quant Sale Order",
    "version": "15.0.1.0.0",
    "author": "Quartile Limited",
    "website": "https://www.quartile.co",
    "category": "Sales",
    "license": "AGPL-3",
    "depends": ["sale_stock"],
    "data": [
        "security/ir.model.access.csv",
        "wizard/stock_quant_sale_order_wizard.xml",
    ],
    "installable": True,
}
