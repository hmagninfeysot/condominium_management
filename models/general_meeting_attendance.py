from odoo import api, fields, models, SUPERUSER_ID, _ 

class general_meeting_attendance(models.Model):
    _name = "general.meeting.attendance"
    _description ="General meeting attendance"


    name = fields.Char('Name')
    appartment_id = fields.Many2one('apartment.management',string='Appartment')
    date = fields.Date('Date')
    garage_id = fields.Char('Garage', related='appartment_id.garage')
    parking_space_id = fields.Char('Parking space', related='appartment_id.parking_space')
    homeowner_id = fields.Many2one('res.partner',string='homeowner', related='appartment_id.homeowner')
    share_of_ownership_id = fields.Integer('Share of ownership', related='appartment_id.share_of_ownership')
    meeting_id = fields.Many2one('general.meeting',string='Meeting ID')
    