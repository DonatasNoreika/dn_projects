# -*- coding: utf-8 -*-
from odoo import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

    # Add a new column to the res.partner model, by default partners are not
    # instructors
    # instructor = fields.Boolean("Instructor", default=False)

    project_ids = fields.One2many('dn_projects.project', 'client_id',
        string="Projects", readonly=True)