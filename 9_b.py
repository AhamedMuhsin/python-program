# Try to configure the widget with various options like: bg=”red”, family=”times”, size=18 
from tkinter import *
root = Tk()
def var_states():
    print("male : %d, \nfemale : %d" % (var1.get(),var2.get()))
var1=IntVar()
Checkbutton(root,text="Male",variable=var1).pack()
var2=IntVar()
Checkbutton(root,text="Female",variable=var2).pack()
Button(root,text="Show",command=var_states()).pack()
mainloop()
