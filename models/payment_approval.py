from odoo import api, fields, models, SUPERUSER_ID, _ 

class payment_approval(models.Model):
    _name = "payment.approval"
    _description ="Payment approval"

    name = fields.Char('Name')
    date = fields.Date('Date')
    apartment_id = fields.Many2one('apartment.management',string='Apartment')
    comment = fields.Char('Comment')
    currency_id = fields.Many2one('res.currency',string='Currency')
    montlhy_payment_theorical = fields.Monetary('Montlhy payment theorical', related='apartment_id.montlhy_payment')
    real_payment = fields.Monetary('Real payment')
    homeowner_id = fields.Many2one('res.partner',string='Homeowner', related='apartment_id.homeowner_id')
    state_id = fields.Many2one('payment.state',string='State')