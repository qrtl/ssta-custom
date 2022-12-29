# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
{
    "name": "Product Auction",
    "category": "Auction",
    "version": "15.0.1.0.0",
    "author": "Quartile Limited",
    "website": "https://www.quartile.co",
    "license": "LGPL-3",
    "depends": ["product", "base_auction"],
    "data": [
        "security/ir.model.access.csv",
        "data/menuitem_data.xml",
        "views/battery_service_views.xml",
        "views/product_model_category_views.xml",
        "views/product_model_views.xml",
        "views/product_product_views.xml",
        "views/product_template_views.xml",
        "views/rom_size_views.xml",
        "views/sim_lock_views.xml",
        "views/use_limit_views.xml",
        "views/telecom_carrier_views.xml",
        "views/product_grade_views.xml",
        "views/qa_state_views.xml",
    ],
    "installable": True,
}
