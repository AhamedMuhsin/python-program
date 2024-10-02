#Design a database application to that allows the user to add, delete and modify the records. 
from tkinter import *
from tkinter import messagebox
import mysql.connector as mysql

def put(*args):
    conn=mysql.connect(user='root',password='vivek@12345',host='localhost',database='rahul')
    cursor=conn.cursor()
    cursor.execute("insert into emp(empid,ename,sal) values("+identry.get()+",'"+nameentry.get()+"',"+salentry.get()+")")
    messagebox.showinfo("into msg","record inserted")
    conn.commit()
    conn.close()

win=Tk()
identry=Entry(win,width=7)
identry.grid(row=0,column=1)
nameentry=Entry(win,width=7)
nameentry.grid(row=1,column=1)
salentry=Entry(win,width=7)
salentry.grid(row=2,column=1)
Button(win,text="insert",command=put).grid(row=3,column=1)
win.mainloop()