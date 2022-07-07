# -*- coding: utf-8 -*-


{
    'name': 'Recharge Website',
    'version': '1.0.1',
    'category': '',
    'summary': '',
    'sequence': -100,
    'description': """hello this is recharge website
    """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/recharge.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets': {
        'web._assets_primary_variables': [

        ],
        'web.assets_backend': [
            'Recharge/static/src/css/load.css',

        ],
        'web.assets_frontend': [
            'Recharge/static/src/css/load.css',
        ],
        'web.assets_tests': [

        ],
        'web.qunit_suite_tests': [

        ],
        'web.assets_qweb': [

        ],
    },
    'license': 'LGPL-3',
}
