{
    "name":"uniik_estate",
    "version":"1.0",
    "author":"Theo Mercifield",
    "website": "https://uniiktheo.tech",
    "category":"Real Estate",
    "sequence":-10,
    "summary":"Real Estate Management",
    "description":"""A module to manage real estate properties, clients, and transactions. For a test by Conak Technology""",
    "depends": ["base"],
    "license": "AGPL-3",
    "data": [
        'views/property_views.xml',
        'views/offer_views.xml',
        'security/ir.model.access.csv',
        'data/demo_data.xml',
    ],
    'demo': [
        'data/demo_data.xml',
    ],

    
    "installable": True,
    "application": True
}