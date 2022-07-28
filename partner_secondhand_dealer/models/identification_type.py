# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class IdentificationType(models.Model):
    _name = "identification.type"

    name = fields.Char(required=True)
