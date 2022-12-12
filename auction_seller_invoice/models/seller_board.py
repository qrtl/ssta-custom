# Copyright 2022 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SellerBoard(models.Model):
    _inherit = "seller.board"

    board_type = fields.Selection(selection_add=[("invoice", "Invoices")])
