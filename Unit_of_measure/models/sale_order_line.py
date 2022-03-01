import string
from odoo import _,models,fields,api
from datetime import datetime, timedelta, date
from odoo.exceptions import UserError, ValidationError




class SalOrdeLine(models.Model):
    _inherit = 'sale.order.line'
    
    @api.onchange('product_id')
    def product_id_change(self):
        res = super(SalOrdeLine, self).product_id_change()
        for rec in self:
            partner_product = rec.order_id.partner_id.inventory_line_ids
            sale_product = rec.product_id

        for record in partner_product:
            if sale_product == record[0].product_id:
                rec.product_uom=record[0].uom_id
        return res 