{
    'name': "Project Task",
    'version': '15.0.1.0.0',
    'category': 'Category',
    'depends': ['product','sale_stock','stock'],
    'author': "Pravin Nayee",
    'license': 'LGPL-3',
    'summary': 'Tranning module',
    'description': " Module for perform  odoo task   ",
    'website': 'https://WWW.odoo.com',

    
    'data': [
        "views/task_sepration.xml",
    ],

    'installable': True,
    'auto_install': False,
    'application': True,

}
