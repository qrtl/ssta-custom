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
                sol.product_id
            FROM
                sale_order_line sol
            JOIN
                product_product pp ON sol.product_id = pp.id
            JOIN
                product_template pt ON pp.product_tmpl_id = pt.id
            WHERE
                sol.state in ('sale', 'done')
                AND sol.qty_delivered > 0
                AND pp.active = True
                AND (pt.type = 'product' OR pt.type = 'consu')
            GROUP BY
                sol.product_id
        """
        )

        prod_ids = [r[0] for r in self.env.cr.fetchall()]

        for prod in self.browse(prod_ids):
            # if product has reordering rules then deactivate first
            if prod.orderpoint_ids:
                prod.orderpoint_ids.write({"active": False})
            prod.product_tmpl_id.write({"active": False})
