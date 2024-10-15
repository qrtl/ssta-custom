# Copyright 2024 Quartile (https://www.quartile.co)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import SUPERUSER_ID, api


def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    cancel_pos = env["purchase.order"].search([("state", "=", "cancel")])
    products = cancel_pos.mapped("order_line.product_id")
    products = products.filtered(lambda x: x.qty_available <= 0.0)
    products.write({"active": False})
    products.mapped("product_tmpl_id").write({"active": False})
