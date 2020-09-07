from handler2 import Event
from handler2 import Connection
from handler2 import Utility
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
        self.xblank = prop['prospect']['xblank']
        self.yblank = prop['prospect']['yblank']
    
    def search_element(self, element):
        # Prospects screen
        time.sleep(2)
        Event.click(self.xsearch,self.ysearch)
        time.sleep(2)
        Event.type_keys(self.win, element)
        time.sleep(10)

    def validate_date(self):
        # Prospects screen
        Event.click(443, 349)
        time.sleep(2)
        Event.click(414, 407)
        time.sleep(2)
        Event.click(self.xcontact_date,self.ycontact_date)
        time.sleep(2)
        Event.rclick(self.xcontact_date,self.ycontact_date)
        time.sleep(2)
        Event.click(408,495)
        time.sleep(2)
        Event.rclick(self.xcontact_date,self.ycontact_date)
        time.sleep(2)
        Event.click(self.xcopy1,self.ycopy1)
        time.sleep(2)
        nxt_contact_date = Event.get_clipboard_data()

        Event.click(self.xappointment_date,self.yappointment_date)
        time.sleep(3)
        Event.rclick(self.xappointment_date,self.yappointment_date)
        time.sleep(3)
        Event.click(649,495)
        time.sleep(2)
        Event.rclick(self.xappointment_date,self.yappointment_date)
        time.sleep(2)
        Event.click(self.xcopy2,self.ycopy2)
        time.sleep(3)
        nxt_appointment_date = Event.get_clipboard_data()
        time.sleep(2)

        # Event.click(self.xcontact_date,self.ycontact_date)
        # time.sleep(3)
        # Event.dclick(self.xcontact_date,self.ycontact_date)
        # time.sleep(3)
        # Event.rclick(self.xcontact_date,self.ycontact_date)
        # time.sleep(3)
        # Event.click(self.xcopy1,self.ycopy1)
        # time.sleep(3)
        # nxt_contact_date = Event.get_clipboard_data()
        # Event.click(self.xappointment_date,self.yappointment_date)
        # time.sleep(3)
        # Event.dclick(self.xappointment_date,self.yappointment_date)
        # time.sleep(3)
        # Event.rclick(self.xappointment_date,self.yappointment_date)
        # time.sleep(3)
        # Event.click(self.xcopy2,self.ycopy2)
        # time.sleep(3)
        # nxt_appointment_date = Event.get_clipboard_data()
        # time.sleep(2)

        if nxt_appointment_date == '00/00/00' or nxt_contact_date == '00/00/00':
            return False
        else:
            return True

    def update_date(self):
        Event.click(self.xmodify_date,self.ymodify_date) # Click on Modify Date button
        time.sleep(3)
        # Modify Contact & appointment Dates screen
        Event.click(152,98)
        time.sleep(3)
        Event.type_keys(self.win, '000000')
        time.sleep(3)
        Event.send_keys("{TAB 2}")
        time.sleep(3)
        Event.type_keys(self.win, '0000')
        time.sleep(3)
        Event.send_keys("{TAB 2}")
        time.sleep(3)
        Event.type_keys(self.win, '000000')
        time.sleep(3)
        Event.send_keys("{TAB 2}")
        time.sleep(3)
        Event.type_keys(self.win, '0000')
        time.sleep(3)
        Event.click(self.xupdate,self.yupdate)
        time.sleep(3)

    def add_notes(self, notes):
        Event.click(self.xadd_note, self.yadd_note)
        time.sleep(3)
        Event.type_keys(self.win, notes)
        time.sleep(3)
        Event.click(self.xblank, self.yblank)
        time.sleep(2)

    def date_modify(self, snap):
        pop_up = Event.snap_location(snap)
        time.sleep(3)
        if pop_up is None:
            print("No Pop up, Date modification not needed")
        else:
            Event.click_snap(pop_up)
            time.sleep(2)