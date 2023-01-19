from odoo import fields, models


class Company(models.Model):
    _inherit = "res.company"

    bank_info = fields.Char(
        name="Bank",
    )
    bank_description = fields.Char(
        name="Description",
    )
