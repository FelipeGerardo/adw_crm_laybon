# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class CrmCustomFields(models.Model):
  _inherit = "crm.lead"
