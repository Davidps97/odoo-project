# -*- coding: utf-8 -*-
# from odoo import http


# class Project-management(http.Controller):
#     @http.route('/project-management/project-management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project-management/project-management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('project-management.listing', {
#             'root': '/project-management/project-management',
#             'objects': http.request.env['project-management.project-management'].search([]),
#         })

#     @http.route('/project-management/project-management/objects/<model("project-management.project-management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project-management.object', {
#             'object': obj
#         })
