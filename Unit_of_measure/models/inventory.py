from odoo import _,models,fields,api
from datetime import datetime, timedelta, date
from odoo.exceptions import UserError, ValidationError



class InventoryLine(models.Model):
    _name = "inventory.line"

    partner_id = fields.Many2one("res.partner", string="Partner ID")
    product_id = fields.Many2one("product.product", string="Product ID")
    uom_category = fields.Many2one(related="product_id.uom_id.category_id", string="UOM Category")
    uom_id = fields.Many2one("uom.uom", string="UOM")


    # product_id
    
    # product_uom_category_id
    
