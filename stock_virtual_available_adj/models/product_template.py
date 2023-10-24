# Copyright 2018 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import api, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    @api.depends(
        "product_variant_ids.qty_available",
        "product_variant_ids.virtual_available",
        "product_variant_ids.incoming_qty",
        "product_variant_ids.outgoing_qty",
    )
    def _compute_quantities(self):
        super()._compute_quantities()
        for pt in self:
            pt.virtual_available = 0.00
            for pp in pt.product_variant_ids:
                pt.virtual_available += pp.virtual_available
        return
