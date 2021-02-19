 #-*- coding: utf-8 -*-
from odoo import models, fields, api


class pg_estetica_model(models.Model):
    _inherit = 'estetica.productos_model'

    img = fields.Binary(string="Foto")


