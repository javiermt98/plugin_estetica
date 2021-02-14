# -*- coding: utf-8 -*-
# from odoo import http


# class PluginEstetica(http.Controller):
#     @http.route('/plugin_estetica/plugin_estetica/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/plugin_estetica/plugin_estetica/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('plugin_estetica.listing', {
#             'root': '/plugin_estetica/plugin_estetica',
#             'objects': http.request.env['plugin_estetica.plugin_estetica'].search([]),
#         })

#     @http.route('/plugin_estetica/plugin_estetica/objects/<model("plugin_estetica.plugin_estetica"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('plugin_estetica.object', {
#             'object': obj
#         })
