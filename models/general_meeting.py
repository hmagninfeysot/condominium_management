from odoo import api, fields, models, SUPERUSER_ID, _ 

class general_meeting(models.Model):
    _name = "general.meeting"
    _description ="General meeting"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Name')
    date = fields.Datetime ('Date/Time')
    meeting_place = fields.Char('Meeting place')
    coownership_trustee_id = fields.Many2one('res.partner',string='Co-ownership trustee')
    president_id = fields.Many2one('res.partner',string='President')
    teller_id = fields.Many2one('res.partner',string='Teller')
    secretary_id = fields.Many2one('res.partner',string='Secretary')
    share_of_ownership_attendance = fields.Integer('Share of ownership attendance')
    attendance_line_ids = fields.One2many('general.meeting.attendance', 'meeting_id', string='Meeting ID')
    meeting_preparation = fields.Text('Meeting preparation')
    order_of_the_day = fields.Text('Order of the day')
    report_meeting = fields.Text('Meeting report')
    state = fields.Selection(selection=[('draft', 'Draft'), ('nsd', 'Need supporting documents'), ('validated', 'Validated'), ('cancelled', 'Cancelled')], string='State')
    meeting_type = fields.Selection(selection=[('gm', 'General meeting'), ('meet', 'meeting')], string='Meeting_type')