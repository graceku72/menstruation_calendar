# can use text tag to mark numbers red on calendar widget? can use a dropdown/entry box to enter the date, then click button to turn it red?

month_label = Label(root, text='Month (numerical format): ', font=('calibre', 10, 'normal'))
month_string = StringVar()
month_entry = Entry(root, textvariable=month_string, font=('calibre', 10, 'normal'))
month_label.grid(row = 0, column = 0)
month_entry.grid(row = 0, column = 1)

year_label = Label(root, text='Year (numerical format): ', font=('calibre', 10, 'normal'))
year_string = StringVar()
year_entry = Entry(root, textvariable=year_string, font=('calibre', 10, 'normal'))
year_label.grid(row = 1, column = 0)
year_entry.grid(row = 1, column = 1)


def enter():
    validity_label = Label(root, text='')
    validity_label.grid(row = 8, column = 1)
    try:
        int(year_entry.get())
        validity_label.config(text='')
    except ValueError:
        validity_label.config(text='Please enter a valid year')
        need to figure out how to make this above text go away once a valid year is entered!!

    months: list[str] = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "01", "02", "03", "04", "05", "06", "07", "08", "09"]
    if month_string not in months:
        month_invalid_label = Label(root, text='Please enter a valid month', font=('calibre', 10, 'normal'))
        # need to figure out how to make this above text go away once a valid month is entered!!
        month_invalid_label.grid(row = 5, column = 1)

    month = int(month_string.get())
    year = int(year_string.get())
     
    month_string.set("")
    year_string.set("")

    cal = calendar.month(year, month)
    calendar.setfirstweekday(calendar.SUNDAY)
    cal_label = tk.Label(root,text=cal,font='Consolas 10 bold', justify='left')
    cal_label.grid(row = 10, column = 1, padx = 20)

    cal = Calendar(root, selectmode='day', year=year, month=month, firstweekday='sunday')
    cal.pack(pady=20)


enter_button = Button(root, text='Enter', command=enter)
enter_button.grid(row = 2, column = 1)


def menstruating(): #scrapped code attempts
    selected_date = cal.selection_get()
        # start = cal.get_date()
        # start_label = Label(root, text=start)
        # start_label.pack(pady=20)
    
    # updated_cal = Calendar(root, showweeknumbers=False, selectmode="day", firstweekday="sunday", selectbackground="red")
    # cal.pack(pady=20, fill="both", expand=True)
    #cal.bind("<<DateEntrySelected>>", print_sel)
    
    # red = Canvas(root)
    # red.pack()
    # confirmation = red.create_text(100, 0, text='Selected date has been marked', anchor='nw', font='TkMenuFont', fill='red')
    # # remove text everytime new date is marked: use red.delete(confirmation)
    #     # when mouse clicks on a new date, confirmation should dissapear
    # #red.itemconfigure('menstruating', fill='red')
    # # red.tag_bind('red', '<1>', menstruating)
    # cal.calevent_create(date=selected_date, text="Menstruating", tags=['red'])
 
    #red.insert('1.0', cal)
    # for line in range(3, len(cal.splitlines()) + 1):
    #     red.tag_add("Start", f"{line}.18", f"{line}.20")