import string
from odoo import _,models,fields,api
from datetime import datetime, timedelta, date
from odoo.exceptions import UserError, ValidationError


class Sale_inherit(models.Model):
    _inherit = "sale.order"

    appointment_Date = fields.Datetime()
    commitment_date = fields.Datetime(compute = '_compute_date')

    Zero_stock_approval = fields.Boolean()


    @api.depends("appointment_Date")
    def _compute_date(self):
        for record in self:
            if record.appointment_Date and record.partner_id.days_to_deliver:
                print("**record",record)
                print("date",record.appointment_Date)
                print("***day_deliver",record.partner_id.days_to_deliver)
                record.commitment_date =(((record.appointment_Date) - timedelta(record.partner_id.days_to_deliver)).date())
                print(record.commitment_date)
            else:
                record.commitment_date = ""

                #record.validity = int((record.date_deadline - (record.create_date).date()).days) 
