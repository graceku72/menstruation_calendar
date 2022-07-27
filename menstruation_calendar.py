"""I created this menstrual cycle calendar for a couple reasons. 
For data privacy, I wanted a menstruation calendar for my personal use. 
Further, while the supplemental options provided in existing menstruation apps can be very useful, I opt for something simpler.
I could've chosen to use the calendar app on my phone, but this already holds other events. I wanted a calendar with one purpose and one purpose only: to mark the dates of menstruation."""

from tkinter import *
from tkcalendar import *
import json
from datetime import datetime

root = Tk()
root.title("Menstrual Cycle Calendar")
root.geometry("400x300+400+100")
root.resizable(False, False)
root.config(background="#EC7063")
window_icon = PhotoImage(file="C:\\Users\\gjku\\personal-coding-projects\\menstruation_calendar\\cal_icon.png")
root.iconphoto(False, window_icon)
# icon link: https://iconarchive.com/show/small-n-flat-icons-by-paomedia/calendar-icon.html
# icon is public domain

cal = Calendar(root, showweeknumbers=False, selectmode="day", firstweekday="sunday", weekendbackground="white", weekendforeground="black", othermonthbackground="light grey", othermonthwebackground="light grey", background="#F0B27A", foreground="black", bordercolor="#F5CBA7", headersbackground="#F5CBA7")
cal.pack(pady=20, fill="both", expand=True)
cal.tag_config("make_red", background="#B30000")

json_list: list[str] = []


def menstruating():
    """Indicates menstruation on the selected date by changing the background color to red."""
    selected_date = cal.selection_get()
    cal.calevent_create(selected_date, "", tags=["make_red"])
    menstruating_button["state"] = DISABLED

    marked_date = cal.get_date()
    json_list.append(marked_date)
    data_file = open("C:\\Users\\gjku\\personal-coding-projects\\menstruation_calendar\\save_cal.json", "w")
    json.dump(json_list, data_file)
    data_file.close()


menstruating_button = Button(root, text="Menstruating", command=menstruating)
menstruating_button.pack(side=LEFT, padx=60, pady=20)


def remove():
    """Reverts a selected date to its original appearance."""
    selected_date = cal.selection_get()
    cal.calevent_remove(tag="make_red", date=selected_date)
    remove_button["state"] = DISABLED

    marked_date = cal.get_date()
    json_list.pop(json_list.index(marked_date))
    data_file = open("C:\\Users\\gjku\\personal-coding-projects\\menstruation_calendar\\save_cal.json", "w")
    json.dump(json_list, data_file)
    data_file.close()


remove_button = Button(root, text="Remove", command=remove, state=DISABLED)
remove_button.pack(side=RIGHT, padx=60, pady=20)


def check_date(event):
    """To determine the state of buttons, checks whether a selected date has been marked red or not."""
    selected_date = cal.selection_get()
    if cal.get_calevents(date=selected_date, tag="make_red"):
        menstruating_button["state"] = DISABLED
        remove_button["state"] = NORMAL
    else:
        menstruating_button["state"] = NORMAL
        remove_button["state"] = DISABLED


cal.bind("<<CalendarSelected>>", check_date)

opening = open("C:\\Users\\gjku\\personal-coding-projects\\menstruation_calendar\\save_cal.json")
cal_events = json.load(opening)
for event in cal_events:
    datetime_date_obj = datetime.strptime(event, "%m/%d/%y")
    cal.calevent_create(datetime_date_obj, "", tags="make_red")
    json_list.append(event)
opening.close()

root.mainloop()