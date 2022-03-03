from odoo import _,fields, models, api
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    
    @api.depends('amount_total','discount','discount_2')
    def _check_total_sale(self):
        for record in self:
            if record.ammount_total:
                new_ammount=record.ammount_total%10
                record.ammount_total=record.new_ammount-1




 



        # print("**************************",self.amount_total)
        # total_ammount = self.amount_total + self.partner_id.credit
        # if total_ammount > self.partner_id.credit_limit:
        #     raise UserError("Total can't greater than credit limit")













    # @api.constrains('amount_total')
    # def _check_total_sale(self):
    #     print("**************************",self.amount_total)
    #     total_ammount = self.amount_total + self.partner_id.credit
    #     if total_ammount > self.partner_id.credit_limit:
    #         raise UserError("Total can't greater than credit limit")