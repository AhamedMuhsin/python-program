from tkinter import *

root = Tk()
s1=Scale(root,from_=0,to=50)
s1.pack()
s2=Scale(root,from_=0,to=200,orient=HORIZONTAL)
s2.pack()
def sel():
    print(s1.get())
    print(s2.get())
Button(root,text='get scale value',command=sel).pack()
mainloop()