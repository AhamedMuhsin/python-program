# Try to configure the widget with various options like: bg=”red”, family=”times”, size=18 
from tkinter import *
root = Tk()
t = Text(root,height=3,width=50)
t.pack()
t.insert(END,"hello\neveryone\n")
farme = Frame(root)
farme.pack()
b1 = Button(farme,text="one",bg="red")
b1.pack()
root.mainloop()
 