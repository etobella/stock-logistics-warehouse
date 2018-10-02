# Copyright 2018 Creu Blanca
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    'name': 'Stock Request kanban',
    'version': '11.0.1.0.1',
    'category': 'Reporting',
    'website': 'https://github.com/OCA/stock-logistics-warehouse',
    'author': 'Creu Blanca, Eficent, Odoo Community Association (OCA)',
    'license': 'AGPL-3',
    'summary': 'Adds a stock request order, and takes stock requests as lines',
    'depends': [
        'stock_request_kanban',
    ],
    'data': [
        'data/stock_data.xml',
        'data/stock_data.yml',
        'data/stock_request_data.xml',
    ],
    'installable': True,
    'application': False,
}
