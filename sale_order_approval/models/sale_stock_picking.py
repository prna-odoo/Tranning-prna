import string
from odoo import _,models,fields,api
from datetime import datetime, timedelta, date
from odoo.exceptions import UserError, ValidationError



class Stock_picking(models.Model):
    _inherit = "stock.picking"

    #appointment_Date = fields.Datetime(string="Appointment Date" , compute="_date_set")
    appointment_Date = fields.Datetime(related='sale_id.appointment_Date',readonly=False ,store=True)


    scheduled_date=fields.Datetime(compute="_compute_schedule_date")

    @api.depends('appointment_Date')
    def _compute_schedule_date(self):
        for record in self:
            if record.scheduled_date and record.partner_id.days_to_deliver :
                record.scheduled_date = record.appointment_Date - timedelta(days=record.partner_id.days_to_deliver)
    # @api.depends("appointment_Date")
    # def _date_set(self):
    #     for record in self:
    #         print("******id is***",record.sale_id )
    #         # if record.picking_type_id:
    #         record.appointment_Date= datetime.now()
    #         # record.appointment_Date= record.sale_id