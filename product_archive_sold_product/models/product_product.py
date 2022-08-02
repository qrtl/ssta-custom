# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    @api.model
    def _process_product_archive(self):
        self.env.cr.execute(
            """
            SELECT
                product_id,
                sum(qty_delivered) AS sale_qty
            FROM
                sale_order_line
            JOIN
                product_product ON product_product.id = sale_order_line.product_id
            WHERE
                state in ('sale', 'done') AND active = True
            GROUP BY
                product_id
        """
        )

        sale_dict = self.env.cr.dictfetchall()

        sale_vals = {}
        for dictionaly in sale_dict:
            sale_vals[dictionaly["product_id"]] = dictionaly["sale_qty"]

        for prod in self.search([("active", "=", True)]):
            if sale_vals.get(prod.id, 0) > 0:
                # if product has reordering rules then deactivate first
                if prod.orderpoint_ids:
                    prod.orderpoint_ids.write({"active": False})
                prod.product_tmpl_id.write({"active": False})
