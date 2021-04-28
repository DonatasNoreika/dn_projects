
from odoo import models, fields, api

class Invoice(models.Model):
    _name = 'dn_projects.invoice'
    _description = "Invoices"

    name = fields.Char(string="Title", required=True)
    total = fields.Float(string="Total")
    status = fields.Selection([
        ('draft', "Draft"),
        ('sent', "Sent"),
        ('paid', "Paid"),
        ('cancelled', "Cancelled"),
    ], string="Progress", default='draft', translate=True)

    project_id = fields.Many2one('dn_projects.project', string="Project")