from tkinter import *
from tkinter.ttk import *

form = Tk()
form.geometry("600x600")
form.title("Form")
form.resizable(width=False,height=False)
label = Label(form, text="Name:")
name_entry = Entry(form)
label.grid(row=0,column=0)
name_entry.grid(row=1,column=0)
form.mainloop()