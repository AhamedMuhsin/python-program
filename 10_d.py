from tkinter import *
import mysql.connector as mysql
def put():
    cur=conn.curosr()
    str="updata student set age=20 where id="+idEntry.get()+""
    cur.execute(str)
    messagebox.showinfo("info msg","record updated")
    conn.commit()
    conn.close()

root = Tk()
root.title("Student Database")
Label(root,text='id').grid(row=0,column=0)
identry=Entry(root,width=10)
identry.grid(row=0,column=1)
Button(root,text='update',command=put).grid(row=0,column=2)
mainloop()