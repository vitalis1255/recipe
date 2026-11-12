from tkinter import *#This imports the tkinter library into the global namespace
from tkinter.ttk import *#This imports ttk or themed TK widget library. This is going to used throughout. ttk is because we want to use beautiful ttk widgets.

root = Tk()#This creates our root or  master application object ie root window
root.title("Learn")
root.geometry("800x600")
label = Label(root, text="Hello, Izuchukwu")
label.pack()#This places the label widget onto its parent widget known as root
label2 = Label(root, text="You are welcome")
label2.pack()
label3 = Label(root,text="Wonderful")
label3.pack()
ent = Entry(root)
ent.pack()
btn = Button(root, text="Submit")
btn.pack()

spn = Spinbox(root,from_=0.5,to=52.0,increment=0.01,textvariable="my_text_var")
spn.pack()

com = Combobox(root, values=["option 1","option 2","option 3","option 4"])
com.pack()

check = Checkbutton(root,text="Check this button to true",variable="my_boolean_var")
check.pack()

my_text = Text(root)
my_text.insert('1.0', ' I love my text widget')
my_text.insert('1.2',' REALLY')
my_text.pack()

sub = Button(root, text="Clear")
sub.pack()

lab1 = LabelFrame(root,text="Button")
lab1.pack()
my_button7 = StringVar()
def mysweet():
  if my_button7.get() == "Hi":
    my_button7.set("There")
  else:
    my_button7.set("Hi")

bbn = Button(root,text="Submit",textvariable=my_button7,command=mysweet)
bbn.pack()



#CREATING A BETTER HELLO WORLD TKINTER: By subclassing Tkinter widgets
root.mainloop()#This is the execution event loop