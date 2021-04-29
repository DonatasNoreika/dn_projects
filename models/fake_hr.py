# -*- coding: utf-8 -*-
from odoo import fields, models

class DN_EmployeePublic(models.Model):
    _inherit = 'hr.employee.public'

    leader = fields.Boolean("Leader", default=False)

    project_ids = fields.Many2many('dn_projects.project',
                                  string="Projects", readonly=True)