from tkinter import *
import datetime
from schedule import *

def activ_button():
    if activity.get() and productivity.get() and time.get():
        new_user.add_task(Task(activity.get(), time.get(), int(productivity.get())))
        activity.delete(0, END)
        time.delete(0, END)
        productivity.delete(0, END)
        calcVar.set(str(new_user.curr_day().productivity))
    else:
        print('ERROR')

new_user = User('Bob', 3)
new_user.add_day()

root = Tk()
root.title('Schedule')

topFrame = Frame(root, bg="white")
topFrame.pack(fill=X)
day_label = Label(topFrame, anchor=W, bg="green", font="Times 16", text="Day: " + str(datetime.date.today()))
day_label.pack(fill=X)

botFrame = Frame(root)
botFrame.pack(pady=15, fill=X)

activity_label = Label(botFrame, text="Activity:")
activity_label.grid(row=0, column=0, stick=E)
activity = Entry(botFrame)
activity.grid(row=0, column=1, columnspan=15, padx=5, sticky=W)

activity_button = Button(botFrame, text="Add new activity", command=activ_button)
activity_button.grid(row=0, column=16, rowspan=3, padx=1)

time_label = Label(botFrame, text="Time spent:")
time_label.grid(row=1, column=0, sticky=E)
time = Entry(botFrame, width=3)
time.grid(row=1, column=1, sticky=W, padx=5)

productivity_label = Label(botFrame, text="Productivity:")
productivity_label.grid(row=1, column=2, sticky=W)
productivity = Entry(botFrame, width=3)
productivity.grid(row=1, column=3, sticky=W, padx=3)

calc_label = Label(botFrame, text="Productivty:")
calc_label.grid(row=2, column=0, stick=E)
calcVar = StringVar()
calc = Label(botFrame, textvariable=calcVar)
calc.grid(row=2, column=1, stick=W, columnspan=4)

root.mainloop()
