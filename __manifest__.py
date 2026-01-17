{
    'name': 'Customer Follow-up Reminder Automation',
    'version': '1.0',
    'summary': 'Automatic customer follow-up reminder with configurable days and dynamic message',
    'description': """
        Automatically send customer follow-up reminders using scheduled cron jobs.
        Supports dynamic message templates and configurable follow-up days.
        """,
    'category': 'CRM',
    'author': 'Minimal Dev',
    'depends': ['base', 'crm'],
    'data': [
        'data/cron.xml',
        'security/ir.model.access.csv',
        'views/followup_view.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
