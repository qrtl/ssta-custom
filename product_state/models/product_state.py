# Copyright 2017-2018 Quartile Limited
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import api, fields, models
from odoo.osv import expression


class ProductState(models.Model):
    _name = "product.state"
    _description = "Product State"
    _order = "sequence, rank"

    rank = fields.Char(required=True)
    description = fields.Char(required=True)
    sequence = fields.Integer(default=10)
    active = fields.Boolean(default=True)
    company_id = fields.Many2one(
        "res.company",
        default=lambda self: self.env["res.company"]._company_default_get(
            "product.state"
        ),
    )

    def name_get(self):
        res = []
        for record in self:
            res.append((record.id, record.rank + "：" + record.description))
        return res

    @api.model
    def _name_search(
        self, name, args=None, operator="ilike", limit=100, name_get_uid=None
    ):
        args = args or []
        domain = []
        if name:
            domain = ["|", ("rank", operator, name), ("description", operator, name)]
        product_states = self._search(
            expression.AND([domain, args]), limit=limit, access_rights_uid=name_get_uid
        )
        return product_states
