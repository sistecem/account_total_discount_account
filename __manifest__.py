# -*- coding: utf-8 -*-
#################################################################################

{
    'name': "Account Total Discount with Account",
    'category': 'Invoicing Management',
    'summary': """Account Total Discount with Account""",
    'license': 'AGPL-3',
    'description': """ """,
    'version': '14.0.1.0',
    'depends': ['base','account','account_tax_python'],
    'data': ['views/account_invoice_view.xml',
             'views/res_company.xml'],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
