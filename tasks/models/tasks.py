import string
from odoo import _,models,fields,api
from datetime import datetime, timedelta, date
from odoo.exceptions import UserError, ValidationError

class Tasks(models.Model):
    _name = "tasks.model"
    _description= "Tasks model"


    name = fields.Char()


class New_inherit(models.Model):
    _inherit = "res.partner"

    days_to_deliver = fields.Integer()


class sale_inherit(models.Model):
    _inherit = "sale.order"

    appointment_Date = fields.Datetime()
    commitment_date = fields.Datetime(compute = '_compute_date')

    Zero_stock_approval = fields.Boolean()


    @api.depends("appointment_Date")
    def _compute_date(self):
        for record in self:
            print("**record",type(self))
            if record.appointment_Date and record.partner_id.days_to_deliver:
                print("**record",type(record))
                print("date",record.appointment_Date)
                print("***day_deliver",record.partner_id.days_to_deliver)
                record.commitment_date =(((record.appointment_Date) - timedelta(record.partner_id.days_to_deliver)).date())
                print(record.commitment_date)
            else:
                record.commitment_date = ""

                #record.validity = int((record.date_deadline - (record.create_date).date()).days) 


class Stock_picking(models.Model):
    _inherit = "stock.picking"

    #appointment_Date = fields.Datetime(string="Appointment Date" , compute="_date_set")
    appointment_Date = fields.Datetime(related='sale_id.appointment_Date',readonly=False ,store=True)


    scheduled_date=fields.Datetime(compute="_compute_schedule_date")

    @api.depends('appointment_Date')
    def _compute_schedule_date(self):
        for record in self:
            if record.scheduled_date and record.partner_id.days_to_deliver :
                record.scheduled_date = record.appointment_Date - datetime.timedelta(days=record.partner_id.days_to_deliver)
    # @api.depends("appointment_Date")
    # def _date_set(self):
    #     for record in self:
    #         print("******id is***",record.sale_id )
    #         # if record.picking_type_id:
    #         record.appointment_Date= datetime.now()
    #         # record.appointment_Date= record.sale_id