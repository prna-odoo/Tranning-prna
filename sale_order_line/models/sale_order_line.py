from odoo import _,fields, models, api
from odoo.exceptions import UserError


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"
    
    discount_2 = fields.Float()




