- DESCRIPTION:
    This module use birtday and partner's name for
    create birtday events on calendar.
    Add two Scheduled Action: 
        *Contacts Birthday on Calendar: Previus Contacts* it's used only once for create event for contacts with birtdate before install this module.
        *Contacts Birthday on Calendar* it's used for check if a contact have a birtday event for the next year and create if not have it.


- USAGE:
#. Go to *Contact*.
#. In the form view, click on *Personal Information* page.
#. Select a date on *Birthdate* field.
#. Active *Allow Birthdate Notification* field (active by default)
#. In calendar view, active *Everybody's calendars*.


- CONFIGURE (Unused until fix traductions on ir.cron):
For use this module on Spanish follow the next steps:
    #. Active developer mode.
    #. Go to *Settings > Translations > Load a Translation*.
    #. Select *Spanish* for lang field.
    #. If *partner_contact_birthdate* module is previously installed follow the next steps for generate events for previus partner's birthdate:
        #. Go to *Settings > Technical > Scheduled Actions*.
        #. Open the action *Contacts Birthday on Calendar: Previus Contacts*.
        #. Use *Run Manually* button.

To modify Scheduled Action:
#. Active developer mode.
#. Go to *Settings > Technical > Scheduled Actions*.
#. Open the action *Contacts Birthday on Calendar*.
#. Modify *Execute Every* field to change execution interval (optional).
#. Modify *Next Execution Date* field to change execution hour or first execution (optional).


- CONTRIBUTORS
* `Aresoltec Canarias, S.L`_:
    * Inma Sánchez
* `Punt Sistemes, S.L.`_:
    * Carlos Ramos
