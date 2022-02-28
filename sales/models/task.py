import string
from odoo import _,models,fields,api
from datetime import datetime, timedelta, date
from odoo.exceptions import UserError, ValidationError

class Task(models.Model):
    _name = "tasks.model"
    _description= "Tasks model"

    name = fields.Char()