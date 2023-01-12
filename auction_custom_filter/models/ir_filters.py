# Copyright 2023 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class IrFilters(models.Model):
    _inherit = "ir.filters"

    auction_share = fields.Boolean("Share To Auction Users")
