import pandas as pd
import time
from handler2 import Event
from handler2 import Connection
from prospect_service import Prospect

try:
    src_data = str(input('Enter the filename with complete relative path: '))
    if '.csv' not in src_data:
        raise("File is not in csv format, file name should end with .csv")
    else:
        print(src_data)
        print(type(src_data))
    # src_data = "C:\\Users\\TechieSamOfficial\\Downloads\\Prospect _notes_only.csv"
    df_data = pd.read_csv(src_data, sep=',', engine='python', encoding='utf-8', skipfooter=3, error_bad_lines=False, header = 1)
    print(df_data.dtypes)
    obj = Connection('win32', 'rdp')
    win = obj.create_conn()
    time.sleep(3)

    prospect_obj = Prospect(win)
    for index, row in df_data.iterrows():
        search_element = row['Company']
        notes_to_add = row['Note Content']

        print("Search Element = {}".format(search_element))
        print("Notes = {}".format(notes_to_add))

        prospect_obj.search_element(search_element)
        print("Search Complete")

        if prospect_obj.validate_date():
            prospect_obj.update_date()
            print("Updated the Dates.")
        else:
            print("No Need to Update Date.")

   
    # Event.click(143,262)
    # time.sleep(3)
    # Event.click(45,431)
    # time.sleep(3)
    # Event.type_keys(win, "56")
    # time.sleep(3)
    # Event.click(129,639)
    # # win.type_keys("samrat")
    # time.sleep(3)
    # Event.click(209,263)
    # time.sleep(3)
    # Event.click(76,430)
    # time.sleep(3)
    # Event.type_keys(win,"vn")
    # time.sleep(3)
    # Event.click(123,636)
    # time.sleep(3)

    # Event.click(177,280)
    # time.sleep(3)
    # Event.send_keys('^c')
    # time.sleep(3)

    # # get clipboard data
    # print(Event.get_clipboard_data())

    # Event.click(1344,29)
    # time.sleep(3)
    # # print(app2['win']['control'].values)
    # win.minimize()
    # time.sleep(3)

    # win.print_control_identifiers()
except Exception as e:
    Event.pop_message(e)
    print(e)