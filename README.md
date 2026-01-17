Customer Follow-up Reminder Automation
=====================================

Automatically send follow-up reminders to customers using scheduled cron jobs.

Features
--------
- Configurable follow-up days
- Dynamic message templates using {{ }} variables
- Works with Customers and CRM Leads
- Safe internal logging (no external API dependency)
- Easy configuration and management

Usage
-----
1. Go to Follow-up Automation → Follow-up Reminders
2. Create a reminder
3. Set follow-up days
4. Write message using dynamic fields
5. System will automatically send reminders

Example Message
---------------
Hello {{name}}, this is your follow-up reminder.

Compatible With
---------------
- Odoo 16