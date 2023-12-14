# -*- coding: utf-8 -*-

from odoo import models, fields, api

class hire_company(models.Model):
    _name ='hire_company'
    _description = 'Hire Company'

    name = fields.Char(string='Nombre', required = True)
    projects = fields.Many2many('project.project', string='Projects')
    project_quantity = fields.Integer(string='Project Quantity', compute='_compute_project_quantity')

    @api.depends('projects')
    def _compute_project_quantity(self):
        for hire_company in self:
            hire_company.project_quantity = len(hire_company.projects)

class ProjectProject(models.Model):
    _inherit = 'project.project'

    hire_company_id = fields.Many2one('hire_company', string='Hire Company')
    tasks_ids = fields.One2many('project.task', 'project_id', string='Tasks')