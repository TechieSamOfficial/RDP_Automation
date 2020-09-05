from pywinauto import application
import pywinauto.findwindows
import time
from handler import Event
from handler import Connection

try:
    obj = Connection('win32', 'rdp')
    win = obj.create_conn()
    time.sleep(3)
    Event.click(143,262)
    time.sleep(3)
    Event.click(45,431)
    time.sleep(3)
    Event.type_keys(win, "56")
    time.sleep(3)
    Event.click(129,639)
    # win.type_keys("samrat")
    time.sleep(3)
    Event.click(209,263)
    time.sleep(3)
    Event.click(76,430)
    time.sleep(3)
    Event.type_keys(win,"vn")
    time.sleep(3)
    Event.click(123,636)
    time.sleep(3)

    Event.click(177,280)
    time.sleep(3)
    Event.send_keys('^c')
    time.sleep(3)

    # get clipboard data
    print(Event.get_clipboard_data())

    Event.click(1344,29)
    time.sleep(3)
    # print(app2['win']['control'].values)
    win.minimize()
    time.sleep(3)

    # win.print_control_identifiers()
except Exception as e:
    Event.pop_message(e)
    print(e)
    # import datetime
    # win.set_focus()
    # debug_image = win.capture_as_image()
    # debug_image.save('C:\\Users\\TechieSamOfficial\\Desktop\\log\\' + str(int(datetime.datetime.now().timestamp())) + '.png')