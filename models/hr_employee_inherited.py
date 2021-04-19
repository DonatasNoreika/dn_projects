# -*- coding: utf-8 -*-
from odoo import fields, models

class DN_Employee(models.Model):
    _inherit = 'hr.employee'

    # Add a new column to the res.partner model, by default partners are not
    # instructors
    leader = fields.Boolean("Leader", default=False)

    project_ids = fields.Many2many('dn_projects.project',
                                  string="Projects", readonly=True)