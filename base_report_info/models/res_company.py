from odoo import fields, models


class Company(models.Model):
    _inherit = "res.company"

    bank_info = fields.Char("Bank")
    description = fields.Char("Report Description")
