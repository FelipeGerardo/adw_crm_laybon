# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class PartnerCustomFields(models.Model):
  _inherit = "res.partner"

  lb_razon_social       = fields.Char(string="Razón Social", help="Razón Social")
  lb_domicilio_fiscal   = fields.Char(string="Domicilio Fiscal", help="Domicilio Fiscal")
  lb_rfc                = fields.Char( string="RFC", help="RFC")

  

 
  