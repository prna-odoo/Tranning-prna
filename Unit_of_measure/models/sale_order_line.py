from odoo import api,fields,models,api


class SaleOrdeLine(models.Model):
    _inherit = 'sale.order.line'
    
    @api.onchange('product_id')
    def product_id_change(self):
        res = super(SaleOrdeLine, self).product_id_change()
        for rec in self:
            partner_product = rec.order_id.partner_id.inventory_line_ids
            sale_product = rec.product_id

        for record in partner_product:
            if sale_product == record[0].product_id:
                rec.product_uom=record[0].uom_id
        return res 