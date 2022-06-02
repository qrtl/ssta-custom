# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    case_number = fields.Char()
    product_model_id = fields.Many2one("product.model", "Model")
    model_number = fields.Char()
    rom_size_id = fields.Many2one("rom.size", "ROM Size")
    imei = fields.Char("IMEI")
    sim_lock_id = fields.Many2one("sim.lock", "SIM Lock State")
    battery_health = fields.Char()
    battery_service_id = fields.Many2one("battery.service", "Battery Service Display")
    color = fields.Char()
    use_limit_id = fields.Many2one("use.limit", "Use Limit")
