# -*- coding: utf-8 -*-
{
    'name': "DN projects",

    'summary': """Manage projects""",

    'description': """
        DN projects module for managing:
            - projects
            - jobs
            - employees
            - invoices
    """,

    'author': "Donatas Noreika, Code Academy",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'board', 'mail'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/project_view.xml',
        'views/job_view.xml',
        'views/invoice_view.xml',
        'views/inherited_partner_view.xml',
        'views/inherited_hr_employee_view.xml',
        'views/emp_wizard_view.xml',
        'reports/project_report.xml',
        'reports/invoice_report.xml',
        'views/projects_board.xml',
        'mail_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}