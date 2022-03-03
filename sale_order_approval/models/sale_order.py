from odoo import api,fields,models,_


class SaleInherit(models.Model):
    _inherit = "sale.order"

    zero_stock_approval = fields.Boolean(string="Approve")

