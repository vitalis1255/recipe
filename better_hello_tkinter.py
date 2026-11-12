#Subclassing is simply a way of creating a new class based on an existing one, adding or changing only what is different in the new class. We will use subclassing extensively in this book to extend the functionality of Tkinter widgets.
"""
A better hello world for tkinter
"""
import tkinter as tk
from tkinter import ttk


#create a new class called HelloView subclass
class HelloView(tk.Frame):#HelloView class is the master window. Frame is the super class
  """A friendly little module"""

  #CONSTRUCTOR METHOD FOR SUBCLASS
  def __init__(self, parent, *args, **kwargs):

    #CALLING THE CONSTRUCTOR METHOD OF THE SUPER CLASS
    super().__init__(parent, *args, **kwargs)

    #ASSIGNING VARIABLES FOR SUBCLASS
    self.name = tk.StringVar()
    self.hello_string = tk.StringVar()
    self.hello_string.set("Hello world")
    

    #CREATING WIDGETS(OUR VIEW)
    name_label = ttk.Label(self, text="Name:")
    name_entry = ttk.Entry(self, textvariable=self.name)
    ch_button = ttk.Button(self, text="Change", command=self.on_change)#command is used in button. on_change is a callBack function or method.

    #DISPLAY THE TEXT
    hello_label = ttk.Label(self, textvariable=self.hello_string, font=("TKDefaultFont", 30),wraplength=600)#textvariable determines what will be displayed. The wraplength argument specifies how wide the text can be before it wraps to the next line. There is also a rowconfigure() method if you want to make changes to the grid rows.

    #ARRANGE THE CREATED WIDGETS
    name_label.grid(row=0, column=0, sticky=tk.W)
    name_entry.grid(row=0,column=1,sticky=(tk.W + tk.E))#This stretches to fill the width of the column west and east.
    ch_button.grid(row=0,column=2,sticky=tk.E)
    hello_label.grid(row=1,column=0,columnspan=3)#This causes the widgets to span three grid columns.
    #grid() geometry manager is used to add the widgets. It allows us to position widgets on their parent object.
    #Notice by using the StringVar objects we don't have to interact directly with the widgets. This saved us from having to keep a lot of widget references in our class, but, more importantly, our variable could be updated from any number of sources or update any number of destinations without us having to explicitly write code to do so.
  


  #CALLBACK FUNCTION
  def on_change(self):
    """
    This is a callBack function.
    For button click.
    """
    if self.name.get().strip():
      self.hello_string.set("Hello" + " " + self.name.get())
    else:
      self.hello_string.set("Hello world")


#THE ACTUAL APPLICATION CLASS
class MyApplication(tk.Tk):#tk is a module while TK is a class that is subclassed, which is our main application       object.   TK   is   the   root    window    and      does not have a parent but at above, frame has a parent.
 """
  Hello World Main Application
 """
 def __init__(self, *args, **kwards):#constructor for subclass MyApplication
    super(). __init__(*args, **kwards)#constructor for the super class TK
    self.title("Hello Tkinter")
    self.geometry("800x600")
    self.resizable(width=False,height=False)#To prevent resizing the window.

    self.columnconfigure(1, weight=1)#adjusting the grid configuration. columnconfigure() method is used to make changes to a widget's grid columns.  Here, we're telling it to weight column 1 (the second column) more than the others.

    #We finish our application class by adding our view to the main window as follows:
    #calling the instance of HelloView inside the root window which MyApplication.
    HelloView(self).grid(row=0, column=0, sticky=(tk.E + tk.N + tk.W + tk.S))#Because we want the view to fill the application window, our grid() call sticks it to all sides of its cell
    self.columnconfigure(0, weight=1)# columnconfigure() call causes the first column to expand. we've omitted the row and column arguments; without them, and grid() simply uses the first column of the next available row (in this case, 0, 0).


#ACTUAL EXECUTION OF THE CODE
if __name__ == "__main__":
  app = MyApplication()
  app.mainloop()