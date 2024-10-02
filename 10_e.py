from tkinter import *
import mysql.connector as mysql
def put():
    conn=mysql.connect(user='pallavi',host='localhost',database='college_db')
    cur=conn.curosr()
    str="delete from student where id="+idEntry.get()+""
    cur.execute(str)
    messagebox.showinfo("info msg","record updated")
    conn.commit()
    conn.close()

root = Tk()
root.title("dalete data")
Label(root,text='id').grid(row=0,column=0)
identry=Entry(root,width=10)
identry.grid(row=0,column=1)
Button(root,text='delete',command=put).grid(row=0,column=2)
mainloop()
