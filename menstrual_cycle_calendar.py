# 7/11/2022 commit

"""I created this menstrual cycle calendar for a couple reasons. 
For data privacy, I wanted a menstruation calendar for my personal use. 
Further, while the supplemental options provided in existing menstruation apps can be very useful, I opt for something simpler.
I could've chosen to use the calendar app on my phone, but this already holds other events. I wanted a calendar with one purpose and one purpose only: to mark the dates of menstruation."""

from tkinter import *
from tkcalendar import *
#from tkinter import filedialog
#from configparser import ConfigParser

root = Tk()
root.title("Menstrual Cycle Calendar")
root.geometry("400x300")
root.resizable(False, False)
root.config(background="#EC7063")
window_icon = PhotoImage(file="C:\\Users\\gjku\\personal-coding-projects\\menstruation_cal\\cal_icon.png")
root.iconphoto(False, window_icon)
# icon link: https://iconarchive.com/show/small-n-flat-icons-by-paomedia/calendar-icon.html
#   says that its public domain

# parser = ConfigParser()
# parser.read("savecal.ini")
#saved_cal = parser.get("colors", "cal")

cal = Calendar(root, showweeknumbers=False, selectmode="day", firstweekday="sunday", weekendbackground="white", weekendforeground="black", othermonthbackground="light grey", othermonthwebackground="light grey", background="#F0B27A", foreground="black", bordercolor="#F5CBA7", headersbackground="#F5CBA7")
# change cal font?
cal.pack(pady=20, fill="both", expand=True)


def remove():
    """Reverts a selected date to its original appearance."""
    selected_date = cal.selection_get()
    cal.tag_config("remove", background="white", foreground="black")
    cal.calevent_create(selected_date, "", tags=["remove"])
    remove_button["state"] = DISABLED
    menstruating_button["state"] = NORMAL
    # cal.calevent_remove(selected_date)
        #   when this funct is a part of menstruacting funct, why wont red background color go away when using this method?? - ask on stack exchange??


remove_button = Button(root, text="Remove", command=remove, state=DISABLED)
# change button font?
remove_button.pack(side=RIGHT, padx=60, pady=20)


def menstruating():
    """Indicates menstruation on the selected date by changing the background color to red."""
    selected_date = cal.selection_get()
    cal.tag_config("selected", background='#B30000')
    cal.calevent_create(selected_date, "", tags=["selected"])
    remove_button["state"] = NORMAL
    menstruating_button["state"] = DISABLED
    # enable menstruating button when mouse is clicked on new date that does not have red background & disable the remove button


menstruating_button = Button(root, text="Menstruating", command=menstruating)
# change button font?
menstruating_button.pack(side=LEFT, padx=60, pady=20)


def save_and_exit():
    root.destroy()
# fix this so it actually saves, look up: how to save actions done in tkinter window before exiting
# may have to create a button for this?
# how to do autosave?
    #file_name = filedialog.asksaveasfilename(initialdir="C:/personal_projects/data", title="Save Changes", filetypes=(("Dat Files", "*.dat"), ("All Files", "*.*")))


root.mainloop()