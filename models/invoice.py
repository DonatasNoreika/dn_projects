
from odoo import models, fields, api

class Invoice(models.Model):
    _name = 'dn_projects.invoice'
    _description = "Invoices"

    name = fields.Char(string="Title", required=True)
    total = fields.Float(string="Total")

    project_id = fields.Many2one('dn_projects.project', string="Project")