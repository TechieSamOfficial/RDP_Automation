from pywinauto import application
import pywinauto.mouse as mouse
import pywinauto.keyboard as keyboard
import pyautogui as pya
import win32clipboard
import ctypes
import datetime

class Event(object):
    
    @staticmethod
    def mouse_move(x,y):
        pya.moveTo(x,y)

    @staticmethod
    def click(x,y):
        Event.mouse_move(x,y)
        pya.click(x,y)
    
    @staticmethod
    def dclick(x,y):
        Event.mouse_move(x,y)
        pya.doubleClick(x,y)

    @staticmethod
    def rclick(x,y):
        Event.mouse_move(x,y)
        pya.click(x,y,button='right')

    @staticmethod
    def send_keys(k):
        keyboard.send_keys(k)

    @staticmethod
    def get_clipboard_data():
        win32clipboard.OpenClipboard()
        data = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        return data

    @staticmethod
    def pop_message(msg, type='Error'):
        ctypes.windll.user32.MessageBoxW(0, u"{}".format(msg), u"{}".format(type), 0)

    @staticmethod
    def type_keys(window, k):
        window.type_keys(k, with_spaces=True)
    
    @staticmethod
    def focus(window):
        window.set_focus()

    @staticmethod
    def snap_location(snap):
        return pya.locateOnScreen(snap)
    
    @staticmethod
    def click_snap(snap_location):
        formx, formy = pya.center(snap_location)
        pya.click(formx, formy)

    @staticmethod
    def capture_screen(window):
        window.set_focus()
        debug_image = window.capture_as_image()
        debug_image.save('C:\\Users\\TechieSamOfficial\\Desktop\\log\\' + str(int(datetime.datetime.now().timestamp())) + '.png')

class Connection(object):
    def __init__(self,app_backend, app):
        if app == 'rdp':
            self.app_title = "Remote Desktop Connection"
        self.backend = app_backend
        self.app_path = r"C:\Windows\System32\mstsc.exe"

    def create_conn(self):
        app = application.Application(backend="{}".format(self.backend)).connect(path = r"{}".format(self.app_path))
        win = app.window(title_re='.*{}'.format(self.app_title))
        win.maximize()
        return win

class Utility():

    @staticmethod
    def is_null(data):
        if data is None:
            return True
        elif not data.strip():
            return True
        else:
            return False
 