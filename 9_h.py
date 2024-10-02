from tkinter import *
root = Tk()
s1 = Spinbox(root,from_=0,to=5)
s1.pack()
s2= Spinbox(values=(2,3,5,7))
s2.pack()
mainloop()
