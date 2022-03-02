from odoo import models, api
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.constrains('amount_total')
    def _check_total_sale(self):
        print("**************************",self.amount_total)
        total_ammount = self.amount_total + self.partner_id.credit
        if total_ammount > self.partner_id.credit_limit:
            raise UserError("Total can't greater than credit limit")