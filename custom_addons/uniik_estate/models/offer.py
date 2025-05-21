from odoo import models, fields, api
from datetime import timedelta

class EstatePropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Property Offer'
    _order = 'price desc'

    price = fields.Float(string='Offer Price', required=True)
    status = fields.Selection(
        [('accepted', 'Accepted'), ('refused', 'Refused')],
        string='Status', copy=False)
    partner_id = fields.Many2one('res.partner', string='Customer', required=True)
    property_id = fields.Many2one('estate.property', string='Property', required=True)
    deadline = fields.Date(string='Deadline')

    @api.model
    def create(self, vals):
        if 'deadline' not in vals:
            vals['deadline'] = fields.Date.today() + timedelta(days=7)
        return super().create(vals)
