
from odoo import models, fields, api

class Project(models.Model):
    _name = 'dn_projects.project'
    _description = "Projects"

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")

    leader_id = fields.Many2one('hr.employee', string="Team Leader", domain=[('leader', '=', True)])
    client_id = fields.Many2one('res.partner', string="Client")

    jobs_ids = fields.One2many('dn_projects.job', 'project_id', string="Jobs")
    invoice_ids = fields.One2many('dn_projects.invoice', 'project_id', string="Invoices")
    employees_ids = fields.Many2many('hr.employee', string="Employees")
    
