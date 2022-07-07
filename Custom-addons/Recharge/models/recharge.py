from odoo import api, models, fields


class Recharge(models.Model):
    _name = 'recharge.recharge'

    name = fields.Char(string='Name')
    destination = fields.Char(string='Destination')
    start_date = fields.Char(string='Start Date')
    end_date = fields.Char(string='End Date')
