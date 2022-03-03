from odoo import _,models,fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    # Fields declarations
    days_to_deliver = fields.Integer(string="Date of deliver")


