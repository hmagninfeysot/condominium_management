from odoo import api, fields, models, SUPERUSER_ID, _ 

class general_meeting_attendance(models.Model):
    _name = "general.meeting.attendance"
    _description ="General meeting attendance"

    name = fields.Char('Name')
    apartment_id = fields.Many2one('apartment.management',string='Apartment')
    date = fields.Date('Date')
    garage = fields.Char('Garage', related='apartment_id.garage')
    parking_space = fields.Char('Parking space', related='apartment_id.parking_space')
    homeowner_id = fields.Many2one('res.partner',string='Homeowner', related='apartment_id.homeowner_id')
    share_of_ownership = fields.Integer('Share of ownership', related='apartment_id.share_of_ownership')
    meeting_id = fields.Many2one('general.meeting',string='Meeting ID')