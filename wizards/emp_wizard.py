# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Wizard(models.TransientModel):
    _name = 'dn_projects.emp_wizard'
    _description = "Wizard: Quick Add of Employees to Projects"

    def _default_projects(self):
        return self.env['dn_projects.project'].browse(self._context.get('active_ids'))

    project_ids = fields.Many2many('dn_projects.project',
                                   string="Projects", required=True, default=_default_projects)
    employee_ids = fields.Many2many('hr.employee', string="Employees")

    def add_emp(self):
        for project in self.project_ids:
            project.employees_ids |= self.employee_ids
        return {}