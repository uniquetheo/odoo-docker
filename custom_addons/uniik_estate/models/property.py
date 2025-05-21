from odoo import models, fields

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Real Estate Property'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    property_type = fields.Selection([
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('land', 'Land'),
    ], string="Property Type", default='house')
    price = fields.Float(string="Price", required=True)
    status = fields.Selection([
        ('available', 'Available'),
        ('sold', 'Sold'),
        ('rented', 'Rented'),
    ], string="Status", default='available')

    offer_ids = fields.One2many('estate.property.offer', 'property_id', string='Offers')

