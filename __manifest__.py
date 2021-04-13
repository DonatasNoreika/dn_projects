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

    'author': ["Donatas Noreika", "Code Academy"],
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'templates.xml',
        'views/project_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
}