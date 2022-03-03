from odoo import api,models
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.constrains('amount_total')
    def _check_total_sale(self):
        total_ammount = self.amount_total + self.partner_id.credit
        if total_ammount > self.partner_id.credit_limit:
            raise UserError("Total can't greater than credit limit")