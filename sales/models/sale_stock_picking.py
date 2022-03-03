import datetime
from odoo import api,fields,models,_



class StockPicking(models.Model):
    _inherit = "stock.picking"

    # Fields declarations
    appointment_Date = fields.Datetime(related='sale_id.appointment_Date',readonly=False, store=True)
    scheduled_date=fields.Datetime(compute="_compute_schedule_date")

    @api.depends('appointment_Date')
    def _compute_schedule_date(self):
        for record in self:
            if record.appointment_Date and record.partner_id.days_to_deliver > 0:
                record.scheduled_date = record.appointment_Date - datetime.timedelta(days=record.partner_id.days_to_deliver)
            else:
                record.scheduled_date=""
    