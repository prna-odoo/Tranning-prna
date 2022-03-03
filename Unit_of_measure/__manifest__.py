{
    'name': "Unit of measure",
    'version': '15.0.1.0.0',
    'category': 'Category',
    'depends': ['product','sale_stock','stock'],
    'author': "Pravin Nayee",
    'license': 'LGPL-3',
    'summary': 'Tranning module',
    'description': """ Module for perform  odoo task   """,
    'website': 'https://WWW.odoo.com',

    
    'data': [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/res_partner_views.xml",
        "views/sale_order_views.xml",
        "views/inventory_add_appointment_date_views.xml",
        "views/sale_approval_views.xml",
        "views/unit_of_measure_views.xml",
    ],

    'installable': True,
    'auto_install': False,
    'application': True,

}
