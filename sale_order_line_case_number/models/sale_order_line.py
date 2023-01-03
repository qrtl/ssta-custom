# Copyright 2023 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def get_sale_order_line_multiline_description_sale(self, product):
        description = super(
            SaleOrderLine, self
        ).get_sale_order_line_multiline_description_sale(product)
        if product.case_number:
            if not product.default_code:
                description = "[" + product.case_number + "] " + description
                return description
            pos = description.find("]")
            description = (
                description[: pos + 1]
                + "["
                + product.case_number
                + "]"
                + description[pos + 1 :]
            )
            return description
        return description
