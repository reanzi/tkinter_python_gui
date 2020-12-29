# from tkinter import *
# from tkinter import ttk
# import tkinter.messagebox as message
# import mysql.connector as mysql

# # root = tkinter.Tk()
# tkinter.geometry("600x300")
# tkinter.title("Fisheries Recordes")
# tkinter._test()

from tkinter import *
from tkinter import ttk
import tkinter.messagebox as message
import mysql.connector as mysql
from PIL import ImageTk, Image



root = Tk()
# logo = PhotoImage(file='./img/green_fishing.jpg')
logo = ImageTk.PhotoImage(Image.open("./img/logo.PNG"))

# Setting icon of root window
root.iconphoto(False, logo)

root.title("Fisheries Records")
# root.geometry('800x600-5+40')
root.geometry('800x500')

# Functions
def insert():
    pass
def get():
    pass
def update():
    pass
def delete():
    pass


# Id field
Heading = Label(root,text="Create New User", font=("bold", 25))
Heading.place(x=100,y=10)
# Id field
id = Label(root,text="enter ID", font=("bold", 12))
id.place(x=20,y=80)
e_id = Entry()
e_id.place(x=160, y=80)

# Id field
name = Label(root,text="enter name", font=("bold", 12))
name.place(x=20,y=110)
e_name = Entry()
e_name.place(x=160, y=110)

# Id field
phone = Label(root,text="enter phone", font=("bold", 12))
phone.place(x=20,y=140)
e_phone = Entry()
e_phone.place(x=160, y=140)

# Id field
address = Label(root,text="enter address", font=("bold", 12))
address.place(x=20,y=170)
e_address = Entry()
e_address.place(x=160, y=170)

insert = Button(root, text="Insert", font=("thin", 12), bg="white", command=insert)
insert.place(x=30, y=240)
get = Button(root, text="Get", font=("thin", 12), bg="white", command=get)
get.place(x=90, y=240)
update = Button(root, text="Update", font=("thin", 12), bg="white", command=update)
update.place(x=140, y=240)
delete = Button(root, text="Delete", font=("thin", 12), bg="white", command=delete)
delete.place(x=220, y=240)


















mainframe = ttk.Frame(root, padding="3 3 12 12")
def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass




# mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)

# feet = StringVar()
# feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
# feet_entry.grid(column=2, row=1, sticky=(W, E))

# meters = StringVar()
# ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

# ttk.Button(mainframe, text="Calculate", command=calculate).grid(
#     column=3, row=3, sticky=W)

# ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
# ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
# ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# for child in mainframe.winfo_children():
#     child.grid_configure(padx=5, pady=5)

# feet_entry.focus()
# root.bind("<Return>", calculate)

root.mainloop()
