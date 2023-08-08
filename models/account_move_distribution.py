from odoo import api, fields, models, SUPERUSER_ID, _ 

class account_move_distribution(models.Model):
    _name = "account.move.distribution"
    _description ="Account move distribution"

    name = fields.Char('Name', compute='_set_name') 
    apartment_id = fields.Many2one('apartment.management',string='Apartment')
    homeowner_id = fields.Many2one('res.partner',string='Homeowner', related='apartment_id.homeowner_id')
    share_of_ownership = fields.Integer('Share of ownership', related='apartment_id.share_of_ownership')
    account_move_id = fields.Many2one('account.move',string='Account move ID')
    date = fields.Date('Date', related='account_move_id.invoice_date')
    amount_total = fields.Monetary('Total amount', related='account_move_id.amount_total')
    ref = fields.Char('Bill reference', related='account_move_id.ref')
    partner_id = fields.Many2one('res.partner', related='account_move_id.partner_id')
    distribution_amount = fields.Monetary('Distribution amount',  compute='_compute_distribution_amount')
    currency_id = fields.Many2one('res.currency',string='Currency', related='account_move_id.currency_id')

    @api.depends('account_move_id.share_of_ownership_total')
    def _compute_distribution_amount(self):
        for record in self:
            if record.account_move_id.share_of_ownership_total > 0:
                record['distribution_amount']=(record.share_of_ownership * record.amount_total) / record.account_move_id.share_of_ownership_total
            else:
                record['distribution_amount'] = 0

    @api.depends('apartment_id', 'distribution_amount', 'ref')
    def _set_name(self):
        for record in self :
            if record.apartment_id and record.distribution_amount and record.ref:
                record.name = f"{record.apartment_id.name} - {record.distribution_amount} - {record.ref}"
            else:
                record.name = "/"