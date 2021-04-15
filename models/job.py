
from odoo import models, fields, api

class Job(models.Model):
    _name = 'dn_projects.job'
    _description = "Jobs"

    name = fields.Char(string="Title", required=True)

    project_id = fields.Many2one('dn_projects.project', string="Project")