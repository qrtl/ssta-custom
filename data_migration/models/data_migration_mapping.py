# Copyright 2023 Quartile Limited
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class DataMigrationMapping(models.AbstractModel):
    _name = "data.migration.mapping"

    def map_many2one_field_by_name(self, env, model_name, field_value):
        """
        Return the ID of a record in the specified model based on its name.

        :param env: Odoo environment.
        :param model_name: The name of the model (e.g., 'res.partner').
        :param field_value: Tuple containing the ID and name of the record in the old system.
        :return: ID of the record in the new system with the same name.
        """

        if not isinstance(field_value, (tuple, list)):
            return field_value

        old_id, name = field_value
        if model_name == "res.partner":
            record = env[model_name].search(
                [("old_id", "=", old_id), ("active", "in", [True, False])], limit=1
            )
        else:
            record = env[model_name].search([("name", "=", name)], limit=1)

        return record.id if record else False
