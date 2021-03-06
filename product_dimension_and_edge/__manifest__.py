# -*- encoding: utf-8 -*-
#    Copyright 2018 Sistemas de Datos - Rodrigo Colombo Vlaeminch <rcolombo@sdatos.es>
#    License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0
{
    'name' : 'Product Dimension And Edge',
    'version' : '0.5',
    'author' : 'Sistemas de Datos',
    'maintainer': 'Sistemas de Datos',
    'category' : 'Product',
    'summary': 'Extension for product_dimension',
    'description' : """
Product Dimension And Edge
==========================

.
""",
    'website': 'http://www.sdatos.com',
    # End General Data
    'depends' : ['sale'],
    'data': ['data/product_uom_data.xml',
             'wizard/dimension_wizard_view.xml',
             'views/sale_order_view.xml'],
    'installable': False,
    'auto_install': False,
    'application': False,
}
