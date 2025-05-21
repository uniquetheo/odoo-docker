{
    "name":"uniik_estate",
    "version":"1.0",
    "author":"Theo Mercifield",
    "category":"Real Estate",
    "sequence":-10,
    "summary":"Real Estate Management",
    "description":"""A module to manage real estate properties, clients, and transactions.""",
    "depends": ["base"],
    "data": [
        'views/property_views.xml',
        # 'security/ir.model.access.csv',
    ],
    "installable": True,
    "application": True
}