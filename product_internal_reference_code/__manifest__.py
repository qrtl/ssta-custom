# Copyright 2022 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Product Internal Reference Code",
    "version": "15.0.1.0.0",
    "category": "Sales",
    "author": "Quartile Limited",
    "website": "https://www.quartile.co",
    "depends": ["product"],
    "license": "AGPL-3",
    "summary": """
        Product is created, system will auto-generate a sequential number for
        default_code.
    """,
    "post_init_hook": "_create_ir_sequence",
    "application": False,
    "installable": True,
}
