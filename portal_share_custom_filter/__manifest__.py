# Copyright 2023 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Portal Share Custom Filter",
    "version": "15.0.1.0.0",
    "category": "Usability",
    "author": "Quartile Limited",
    "website": "https://www.quartile.co",
    "license": "AGPL-3",
    "data": [
        "security/ir.model.access.csv",
        "security/group_portal_security.xml",
        "views/ir_filters_views.xml",
    ],
    "depends": ["base_custom_filter"],
    "installable": True,
}
