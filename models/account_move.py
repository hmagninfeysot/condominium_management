from odoo import api, fields, models, _

class account_move(models.Model):
    _inherit = 'account.move'

    distribution_account_move_ids = fields.One2many('account.move.distribution', 'account_move_id', string='Account move ID')
    share_of_ownership_total = fields.Integer('Share of ownership total', compute='_compute_share_of_ownership_total')

    @api.depends('distribution_account_move_ids')
    def _compute_share_of_ownership_total(self):
        for record in self:
            tantieme_ids=self.env['account.move.distribution'].search([('account_move_id', '=', record.id)])
            if tantieme_ids:
                record['share_of_ownership_total']=(sum(tantieme_ids.mapped('share_of_ownership')))
            else:
                record['share_of_ownership_total']=0  