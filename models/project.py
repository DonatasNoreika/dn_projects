
from odoo import models, fields, api

class Project(models.Model):
    _name = 'dn_projects.project'
    _description = "Projects"

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")