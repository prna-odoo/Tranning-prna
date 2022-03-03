{
    'name': "Sale order line",
    'version': '15.0.1.0.0',
    'category': 'Category',
    'depends': ['product','sale_stock','stock'],
    'author': "Pravin Nayee",
    'license': 'LGPL-3',
    'summary': 'Tranning module',
    'description': """ Module for sale order line """,
    'website': 'https://WWW.odoo.com',

    
    'data': [
        # "security/security.xml",
        # "security/ir.model.access.csv",
        # "views/task_menus_views.xml",
        # "views/res_partner_views.xml",
        "views/sale_order_line_views.xml",
    ],

    'installable': True,
    'auto_install': False,
    'application': True,

}
