from datetime import date, datetime, timedelta
from odoo import api, fields, models, SUPERUSER_ID, _ 

class apartment_management(models.Model):
    _name = "apartment.management"
    _description ="Registration of the apartments of the various condominiums"


    name = fields.Char('Name')
    homeowner = fields.Many2one('res.parntner',string='Homeowner')
    share_of_ownership = fields.Integer('Share of ownership')
    montlhy_payment = fields.Monetary('Montlhy payment')
    payment_submission = fields.Boolean('Payment submission')
    currency_id = fields.Many2one('res.currency',string='Currency')
    garage = fields.Char('Garage')
    parking_space = fields.Char('Parking space')