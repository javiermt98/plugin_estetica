 #-*- coding: utf-8 -*-
from odoo import models, fields, api


class pg_estetica_model(models.Model):
    _inherit = 'estetica.productos_model'
    _name = 'plugin_estetica.pg_estetica_model'
    _description = 'plugin_estetica.plugin_estetica'
    
