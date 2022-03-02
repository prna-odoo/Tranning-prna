from odoo import models, api
from odoo.exceptions import UserError

class AccountMove(models.Model):
    _inherit = "account.move"

    @api.constrains('amount_total')
    def _check_total_reciveable(self):
        total_receivable = self.amount_total + self.partner_id.credit
        if total_receivable > self.partner_id.credit_limit:
            raise UserError("Total receivable can't greater than credit limit")