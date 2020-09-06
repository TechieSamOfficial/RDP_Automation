from handler import Event
from handler import Connection
from handler import Utility
from abstract_service import AbstractService
from config_properties import properties as prop
import time

class Prospect(AbstractService):
    
    def __init__(self, win):
        self.win = win
        self.xsearch = prop['prospect']['xsearch']
        self.ysearch = prop['prospect']['ysearch']
        self.xcontact_date = prop['prospect']['xcontact_date']
        self.ycontact_date = prop['prospect']['ycontact_date']
        self.xcopy1 = prop['prospect']['xcopy1']
        self.ycopy1 = prop['prospect']['ycopy1']
        self.xappointment_date = prop['prospect']['xappointment_date']
        self.yappointment_date = prop['prospect']['yappointment_date']
        self.xcopy2 = prop['prospect']['xcopy2']
        self.ycopy2 = prop['prospect']['ycopy2']
        self.xmodify_date = prop['prospect']['xmodify_date']
        self.ymodify_date = prop['prospect']['ymodify_date']
        self.xadd_note = prop['prospect']['xadd_note']
        self.yadd_note = prop['prospect']['yadd_note']
        self.xupdate = prop['prospect']['xupdate']
        self.yupdate = prop['prospect']['yupdate']
    
    def search_element(self, element):
        # Prospects screen
        Event.click(self.xsearch,self.ysearch)
        time.sleep(2)
        Event.type_keys(self.win, element)
        time.sleep(7)

    def validate_date(self):
        # Prospects screen
        Event.click(self.xcontact_date,self.ycontact_date)
        time.sleep(2)
        Event.dclick(self.xcontact_date,self.ycontact_date)
        Event.rclick(self.xcontact_date,self.ycontact_date)
        Event.click(self.xcopy1,self.ycopy1)
        nxt_contact_date = Event.get_clipboard_data()
        Event.click(self.xappointment_date,self.yappointment_date)
        time.sleep(2)
        Event.dclick(self.xappointment_date,self.yappointment_date)
        Event.rclick(self.xappointment_date,self.yappointment_date)
        Event.click(self.xcopy2,self.ycopy2)
        nxt_appointment_date = Event.get_clipboard_data()

        if nxt_appointment_date == '00/00/00' or nxt_contact_date == '00/00/00':
            return False
        else:
            return True

    def update_date(self):
        Event.click(self.xmodify_date,self.ymodify_date) # Click on Modify Date button
        time.sleep(3)
        # Modify Contact & appointment Dates screen
        Event.click(152,98)
        Event.type_keys(self.win, '000000')
        Event.send_keys("{TAB 2}")
        Event.type_keys(self.win, '0000')
        Event.send_keys("{TAB 2}")
        Event.type_keys(self.win, '000000')
        Event.send_keys("{TAB 2}")
        Event.type_keys(self.win, '0000')
        Event.click(self.xupdate,self.yupdate)

    def add_notes(self, notes):
        pass


