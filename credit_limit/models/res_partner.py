from odoo import _,models,fields,api
from datetime import datetime, timedelta, date
from odoo.exceptions import UserError, ValidationError


class Partner_inherit(models.Model):
    _inherit = "res.partner"


