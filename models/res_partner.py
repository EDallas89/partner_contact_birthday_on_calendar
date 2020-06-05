from odoo import models, fields, api
from datetime import datetime, time, date


class ResPartner(models.Model):
    _inherit = 'res.partner'

    birthdate_date = fields.Date(
        string='Birthday'
    )

    allow_birthdate_notification = fields.Boolean(
        string='Allow Birthdate Notification',
        default=True,
    )

    @api.model
    def create(self, vals):
        res = super().create(vals)
        category = self.env.ref(
            'partner_contact_birthday_on_calendar.categ_meet_birthday')
        if vals['birthdate_date']:
            if vals['allow_birthdate_notification'] == True:
                self.env['calendar.event'].create({
                    'name': 'Cumpleaños Cliente: ' + vals['name'],
                    'start': date.today().strftime("%Y") + vals['birthdate_date'][4:10],
                    'stop': date.today().strftime("%Y") + vals['birthdate_date'][4:10],
                    'allday': True,
                    'show_as': 'free',
                    'recurrency': True,
                    'rrule_type': 'yearly',
                    'count': 2,
                    'partner_ids': False,
                    'user_id': False,
                    'categ_ids': [[4, category.id]],
                })
        return res

    def write(self, vals):
        res = super().write(vals)
        if 'birthdate_date' in vals and vals['birthdate_date']:
            if self.allow_birthdate_notification == True:
                event = self.env['calendar.event'].search([
                    ('name', '=', 'Cumpleaños Cliente: ' + self.name),
                ])
                category = self.env.ref(
                    'partner_contact_birthday_on_calendar.categ_meet_birthday')
                if event:
                    event.write({
                        'active': False,
                    })
                self.env['calendar.event'].create({
                    'name': 'Cumpleaños Cliente: ' + self.name,
                    'start': date.today().strftime("%Y") + vals['birthdate_date'][4:10],
                    'stop': date.today().strftime("%Y") + vals['birthdate_date'][4:10],
                    'allday': True,
                    'show_as': 'free',
                    'recurrency': True,
                    'rrule_type': 'yearly',
                    'count': 2,
                    'partner_ids': False,
                    'user_id': False,
                    'categ_ids': [[4, category.id]],
                })
        return res

    @api.model
    def cron_previus_contacts(self, vals):
        for record in self.search([]):
            if record.birthdate_date:
                category = self.env.ref(
                    'partner_contact_birthday_on_calendar.categ_meet_birthday')
                self.env['calendar.event'].create({
                    'name': 'Cumpleaños Cliente: ' + record.name,
                    'start': date.today().strftime("%Y") + record.birthdate_date.strftime("-%m-%d"),
                    'stop': date.today().strftime("%Y") + record.birthdate_date.strftime("-%m-%d"),
                    'allday': True,
                    'show_as': 'free',
                    'recurrency': True,
                    'rrule_type': 'yearly',
                    'count': 2,
                    'partner_ids': False,
                    'user_id': False,
                    'categ_ids': [[4, category.id]],
                })

    @api.model
    def cron_standard_event(self, vals):
        actual_year = datetime.now().year
        next_year = actual_year + 1
        for record in self.search([]):
            if (record.birthdate_date
                    and record.allow_birthdate_notification):
                event = self.env['calendar.event'].search([
                    ('name', 'ilike', record.name),
                    ('start', '=', str(next_year) +
                     record.birthdate_date.strftime("-%m-%d"))
                ])
                if event:
                    continue
                else:
                    category = self.env.ref(
                        'partner_contact_birthday_on_calendar.categ_meet_birthday')
                    self.env['calendar.event'].create({
                        'name': 'Cumpleaños Cliente: ' + record.name,
                        'start': str(next_year) + record.birthdate_date.strftime("-%m-%d"),
                        'stop': str(next_year) + record.birthdate_date.strftime("-%m-%d"),
                        'allday': True,
                        'show_as': 'free',
                        'partner_ids': False,
                        'user_id': False,
                        'categ_ids': [[4, category.id]],
                    })

    @api.constrains('allow_birthdate_notification')
    def _constrains_allow_birthdate_notification(self):
        if self.allow_birthdate_notification == False:
            event = self.env['calendar.event'].search([
                ('name', '=', 'Cumpleaños Cliente: ' + self.name),
            ])
            if event:
                event.write({
                    'active': False,
                })
        else:
            event = self.env['calendar.event'].search([
                ('name', '=', 'Cumpleaños Cliente: ' + self.name),
                ('active', '=', False)
            ])
            if event:
                event.write({
                    'active': True,
                })
