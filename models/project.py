
from odoo import models, fields, api, exceptions

class Project(models.Model):
    _name = 'dn_projects.project'
    _description = "Projects"

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    max_employees = fields.Integer(string="Max Employees")

    leader_id = fields.Many2one('hr.employee', string="Team Leader", domain=[('leader', '=', True)])
    client_id = fields.Many2one('res.partner', string="Client")

    jobs_ids = fields.One2many('dn_projects.job', 'project_id', string="Jobs")
    invoice_ids = fields.One2many('dn_projects.invoice', 'project_id', string="Invoices")
    employees_ids = fields.Many2many('hr.employee', string="Employees")
    emp_percent = fields.Float(string="Employee percent", compute='_get_employee_percent')

    @api.depends('max_employees', 'employees_ids')
    def _get_employee_percent(self):
        for record in self:
            if not record.max_employees:
                record.emp_percent = 0.0
            else:
                record.emp_percent = 100.0 * len(record.employees_ids) / record.max_employees

    @api.onchange('max_employees', 'employees_ids')
    def _verify_employees_qty(self):
        if self.max_employees < 0:
            return {
                'warning': {
                    'title': "Incorrect 'max employees' value",
                    'message': "The number of max employees may not be negative",
                },
            }
        if self.max_employees < len(self.employees_ids):
            return {
                'warning': {
                    'title': "Too many employees",
                    'message': "Increase max employees or remove excess employees",
                },
            }

    @api.constrains('leader_id', 'employees_ids')
    def _check_leader_not_in_employees(self):
        for r in self:
            if r.leader_id and r.leader_id in r.employees_ids:
                raise exceptions.ValidationError("A project leader can't be an employee")

