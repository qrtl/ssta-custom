# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class RomSize(models.Model):
    _name = "rom.size"
    _description = "ROM Size"

    name = fields.Char()
    active = fields.Boolean(default=True)

    _sql_constraints = [("name", "unique(name)", "Name must be unique!")]
