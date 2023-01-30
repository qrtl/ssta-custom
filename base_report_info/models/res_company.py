# Copyright 2023 Quartile Limited (https://www.quartile.co)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class Company(models.Model):
    _inherit = "res.company"

    bank_info = fields.Text(help="Bank details to supposedly show on custom reports.")
