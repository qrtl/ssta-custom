# Copyright 2023 Quartile
{
    "name": "Commissions Report",
    "version": "15.0.1.0.0",
    "author": "Quartile Limited",
    "category": "Invoicing",
    "license": "AGPL-3",
    "depends": ["product","commission","account"],
    "website": "",
    "maintainers": [],
    "data": [
        "data/report_paperformat_data.xml",
        "data/account_move_data.xml",
        "reports/commission_settlement_report.xml",
        "reports/report_settlement_templates.xml",
        "views/product_template_views.xml",
    ],
    "installable": True,
}
