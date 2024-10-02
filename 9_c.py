# Try to configure the widget with various options like: bg=”red”, family=”times”, size=18 
from tkinter import *
root = Tk()
v = IntVar()
v.set(1) 
languages = [('python',1),('rust',2),('java',3),('c',4),('c++',5)]
def showchoice():
    print("You selected: ", v.get())
label = Label(root, text="Select a programming language:").pack()
for txt,val in languages:
    Radiobutton(root, text=txt, variable=v, command=showchoice(),value=val).pack(anchor=W)
mainloop()
