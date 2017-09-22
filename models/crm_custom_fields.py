# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class CrmCustomFields(models.Model):
  _inherit = "crm.lead"

  lbn_mat_interes		=fields.Char(string="Material de su interes", help="Material de su interes")