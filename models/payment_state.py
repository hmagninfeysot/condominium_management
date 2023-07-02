from odoo import api, fields, models, SUPERUSER_ID, _ 

class payment_state(models.Model):
    _name = "payement.state"
    _description ="payment state"


    name = fields.Char('Name')