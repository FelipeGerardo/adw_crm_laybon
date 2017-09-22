# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class PartnerCustomFields(models.Model):
  _inherit = "res.partner"

  lbn_razon_social       = fields.Char(string="Razón Social", help="Razón Social")
  lbn_domicilio_fiscal   = fields.Char(string="Domicilio Fiscal", help="Domicilio Fiscal")
  lbn_rfc                = fields.Char(string="RFC", help="RFC")
  lbn_nombre_cia		 = fields.Char(string="Nombre CIA", help="Nombre CIA")
  lbn_id                 = fields.Char(string="I.D", help="I.D") 
  lbn_cargo				 = fields.Char(string="Cargo", help="Cargo")
  lbn_giro				 = fields.Char(string="Giro", help="Giro")

  

 
  