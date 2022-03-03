import datetime
from odoo import api,fields,models,_




class SaleInherit(models.Model):
    _inherit = "sale.order"

    # Fields declarations
    appointment_Date = fields.Datetime(string="Appointment Date")
    commitment_date = fields.Datetime(compute = '_compute_date')

    @api.depends("appointment_Date")
    def _compute_date(self):
        for record in self:
            if record.appointment_Date and record.partner_id.days_to_deliver:
                record.commitment_date = record.appointment_Date - datetime.timedelta(days=record.partner_id.days_to_deliver)    
            else:
                record.commitment_date = ""
