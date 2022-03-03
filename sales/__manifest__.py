{
    'name': "Sale Module",
    'version': '15.0.1.0.0',
    'category': 'Category',
    'depends': ['sale'],
    'author': "Pravin Nayee",
    'license': 'LGPL-3',
    'summary': 'Tranning module',
    'description': """ Module for perform  odoo task   """,
    'website': 'https://WWW.odoo.com',

    
    'data': [
        
        "views/res_partner_views.xml",
        "views/sale_order_views.xml",
        "views/inventory_date_views.xml"
    ],

    'installable': True,
    'auto_install': False,
    'application': True,

}
