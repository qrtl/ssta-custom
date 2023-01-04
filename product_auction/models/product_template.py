# Copyright 2022 Quartile Limited
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    case_number = fields.Char()
    product_model_id = fields.Many2one("product.model", "Model")
    product_model_category_id = fields.Many2one(
        related="product_model_id.category_id", store=True
    )
    model_number = fields.Char()
    rom_size_id = fields.Many2one("rom.size", "ROM Size")
    imei = fields.Char("IMEI")
    sim_lock_id = fields.Many2one("sim.lock", "SIM Lock State")
    battery_health = fields.Char()
    battery_service_id = fields.Many2one("battery.service", "Battery Service Display")
    color = fields.Char()
    use_limit_id = fields.Many2one("use.limit", "Use Limit")
    telecom_carrier_id = fields.Many2one("telecom.carrier", "Telecom Carrier")
    product_grade_id = fields.Many2one("product.grade", "Product Grade")
    cpu = fields.Char("CPU")
    ram = fields.Char("RAM")
    qa_state_id = fields.Many2one("qa.state", "QA State")
    qa_note = fields.Text("QA Note")
    description_sale = fields.Text()
