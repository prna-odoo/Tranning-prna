import string
from odoo import _,models,fields,api
from datetime import datetime, timedelta, date
from odoo.exceptions import UserError, ValidationError


class Partner_inherit(models.Model):
    _inherit = "res.partner"

    days_to_deliver = fields.Integer()
    # product_id =fields.One2many("sale.order.line","user_id" ,string="Products")
    inventory_line_ids = fields.One2many("inventory.line","partner_id")


