# Copyright 2022 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Report Account Move with Settlement",
    "version": "15.0.1.0.0",
    "author": "Quartile Limited",
    "category": "Invoicing",
    "license": "AGPL-3",
    "depends": [
        "account",
        "account_commission_listing_fee",
        "base_report_info",
    ],
    "website": "https://www.quartile.co",
    "data": [
        "data/report_paperformat_data.xml",
        "reports/account_move_report.xml",
        "reports/report_settlement_templates.xml",
        "views/res_company_views.xml",
        "views/res_partner_views.xml",
    ],
    "installable": True,
}
