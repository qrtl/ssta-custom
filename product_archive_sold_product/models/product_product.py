# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    # is_sold = fields.Boolean(compute="_compute_is_sold",store=True)
    # #is_sold = fields.Boolean()

    # @api.depends("auction_item_ids")
    # def _compute_is_sold(self):
    #     for product in self:
    #         if product.sales_count == 0:
    #             product.is_sold = False
    #         else:
    #             product.is_sold = True

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
        for dict in sale_dict:
            sale_vals[dict["product_id"]] = dict["sale_qty"]

        for prod in self.search([("type", "=", "product"), ("active", "=", True)]):
            if sale_vals.get(prod.id, 0) > 0:
                # if product has reordering rules then deactivate first
                if prod.orderpoint_ids:
                    prod.orderpoint_ids.write({"active": False})
                prod.product_tmpl_id.write({"active": False})
