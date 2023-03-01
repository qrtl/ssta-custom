# Copyright 2023 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, models
from odoo.exceptions import UserError


class StockRequestOrder(models.Model):
    _inherit = "stock.request.order"

    @api.model
    def _create_from_product_multiselect(self, products):
        if products.filtered(lambda x: not x.seller_id):
            raise UserError(_("Only seller products can be selected."))
        return super()._create_from_product_multiselect(products)
