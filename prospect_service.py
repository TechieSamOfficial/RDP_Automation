from handler import Event
from handler import Connection
from handler import Utility
from abstract_service import AbstractService
import time

class Prospect(AbstractService):
    
    def __init__(self, win):
        self.win = win
    
    def search_element(self, element):
        Event.click(68,196)
        time.sleep(2)
        Event.type_keys(self.win, element)
        time.sleep(7)

    def validate_date(self):
        Event.click(351,382)
        time.sleep(2)
        Event.dclick(351,382)
        Event.rclick(351,382)
        Event.click(396,435)
        nxt_contact_date = Event.get_clipboard_data()
        Event.click(593,382)
        time.sleep(2)
        Event.dclick(593,382)
        Event.rclick(593,382)
        Event.click(630,435)
        nxt_appointment_date = Event.get_clipboard_data()

        if nxt_appointment_date == '00/00/00' or nxt_contact_date == '00/00/00':
            return False
        else:
            return True

    def update_date(self):
        Event.click(754,382) # Click on Modify Date button
        time.sleep(3)
        Event.click(152,98)
        Event.type_keys(self.win, '000000')
        Event.send_keys("{TAB 2}")
        Event.type_keys(self.win, '0000')
        Event.send_keys("{TAB 2}")
        Event.type_keys(self.win, '000000')
        Event.send_keys("{TAB 2}")
        Event.type_keys(self.win, '0000')
        Event.click(95,187)

    def add_notes(self, notes):
        pass


