from odoo import api, fields, models, SUPERUSER_ID, _ 

class account_move_distribution(models.Model):
    _name = "account.move.distribution"
    _description ="Account move distribution"

    name = fields.Char('Name') 
    apartment_id = fields.Many2one('apartment.management',string='Apartment')
    homeowner_id = fields.Many2one('res.partner',string='Homeowner', related='apartment_id.homeowner_id')
    share_of_ownership = fields.Integer('Share of ownership', related='apartment_id.share_of_ownership')
    account_move_id = fields.Many2one('account.move',string='Account move ID')
    date = fields.Date('Date', related='account_move_id.invoice_date')
    amount_total = fields.Monetary('Total amount', related='account_move_id.amount_total')
    ref = fields.Char('Bill reference', related='account_move_id.ref')
    partner_id = fields.Many2one('res.partner', related='account_move_id.partner_id')
    distribution_amount = fields.Monetary('Distribution amount')
    currency_id = fields.Many2one('res.currency',string='Currency')
    
    
    