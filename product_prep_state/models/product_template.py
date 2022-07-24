# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    prep_state_id = fields.Many2one(
        "product.prep.state", string="Preparation State", copy=False
    )
