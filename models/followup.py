import re
from datetime import timedelta
from odoo import api, fields, models
from odoo.fields import Date


class CustomerFollowupReminder(models.Model):
    _name = 'customer.followup.reminder'
    _description = 'Customer Follow-up Reminder'
    _rec_name = 'name'

    name = fields.Char(string="Reminder Name", required=True)
    active = fields.Boolean(default=True)

    model_id = fields.Many2one(
        'ir.model',
        string="Applies To",
        required=True,
        ondelete='cascade'
    )

    followup_days = fields.Integer(
        string="Follow-up After (Days)",
        default=7,
        required=True
    )

    message_body = fields.Text(
        string="Reminder Message",
        required=True,
        default="Hello {{name}}, this is your follow-up reminder."
    )

    last_run = fields.Date(string="Last Reminder Run")

    # ---------------------------------------------------------
    # CORE CRON METHOD
    # ---------------------------------------------------------
    def cron_send_followup_reminder(self):
        reminders = self.search([('active', '=', True)])
        today = Date.today()

        for reminder in reminders:
            model = self.env[reminder.model_id.model]
            target_date = today - timedelta(days=reminder.followup_days)

            domain = [('create_date', '<=', target_date)]
            records = model.search(domain)

            for record in records:
                message = reminder.render_message(record)

                # Example action: Log message (safe for App Store)
                reminder.message_post_safe(record, message)

            reminder.last_run = today

    # ---------------------------------------------------------
    # MESSAGE RENDER ENGINE
    # ---------------------------------------------------------
    def render_message(self, record):
        self.ensure_one()
        message = self.message_body

        variables = re.findall(r'{{(.*?)}}', message)
        for var in variables:
            value = record
            try:
                for field in var.strip().split('.'):
                    value = getattr(value, field)
                message = message.replace('{{%s}}' % var, str(value or ''))
            except Exception:
                message = message.replace('{{%s}}' % var, '')

        return message

    # ---------------------------------------------------------
    # SAFE MESSAGE LOGGER (NO API DEPENDENCY)
    # ---------------------------------------------------------
    def message_post_safe(self, record, message):
        if hasattr(record, 'message_post'):
            record.message_post(body=message)
