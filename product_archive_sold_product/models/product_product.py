# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = "product.product"

    #is_solds = fields.Boolean(compute="_compute_is_sold",store=True)
    is_sold = fields.Boolean()

    @api.depends("auction_item_ids")
    def _compute_is_sold(self):
        for product in self:
            auction_item_ids = product.auction_item_ids
            if auction_item_ids.is_sold == True:
                product.is_solds = True
            else:
                product.is_solds = False

    
    
    
    # @api.model
    # def _process_product_archive(self):
    #     self.env.cr.execute(
    #         """
    #         SELECT
    #             product_id,
    #             sum(product_qty) AS purch_qty
    #         FROM
    #             purchase_order_line
    #         WHERE
    #             state in ('sent', 'draft')
    #         GROUP BY
    #             product_id
    #     """
    #     )
    #     purch_dict = self.env.cr.dictfetchall()

    #     purch_vals = {}
    #     for dict in purch_dict:
    #         purch_vals[dict["product_id"]] = dict["purch_qty"]

    #     for prod in self.search([("type", "=", "product"), ("active", "=", True)]):
    #         if (
    #             prod.virtual_available + purch_vals.get(prod.id, 0) - prod.sent_sale_qty
    #             <= 0
    #         ):
    #             # if product has reordering rules then deactivate first
    #             if prod.orderpoint_ids:
    #                 prod.orderpoint_ids.write({"active": False})
    #             prod.product_tmpl_id.write({"active": False})
