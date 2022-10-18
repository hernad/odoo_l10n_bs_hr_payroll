from odoo import fields, models

class HrContract(models.Model):
    _inherit = 'hr.contract'
    _description = "Employee Contract"

    koef_lo = fields.Float(string="Koef ličnog odbitka", digits="Payroll", default=0.0)
