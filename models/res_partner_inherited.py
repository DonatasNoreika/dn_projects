# -*- coding: utf-8 -*-
from odoo import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

    project_ids = fields.One2many('dn_projects.project', 'client_id',
        string="Projects", readonly=True)