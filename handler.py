from pywinauto import application
import pywinauto.mouse as mouse
import pywinauto.keyboard as keyboard
import win32clipboard
import ctypes

class Event(object):
    
    @staticmethod
    def mouse_move(x,y):
        mouse.move(coords=(x,y))

    @staticmethod
    def click(x,y,butn='left'):
        Event.mouse_move(x,y)
        mouse.click(button=butn,coords=(x,y))
    
    @staticmethod
    def dclick(x,y):
        Event.mouse_move(x,y)
        mouse.double_click(button='left',coords=(x,y))

    @staticmethod
    def rclick(x,y):
        Event.mouse_move(x,y)
        mouse.right_click(coords=(x,y))

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
        window.type_keys(k)
    
    @staticmethod
    def focus(window):
        window.set_focus()

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
    