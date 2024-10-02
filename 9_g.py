from tkinter import *
root = Tk()
lb1 = Listbox(root)
lb1.pack()
listbox=['Grade A',"Grade B","Grade C"]
for v in listbox:
    lb1.insert(END,v)
mainloop()