#Design a simple database application that stores the records and retrieve the same. 

import mysql.connector as mysql

conn=mysql.connect(user='root',password='vivek@12345',host='localhost')
cursor=conn.cursor()
try:
    cursor.execute('create database Ahamed')
    cursor.execute('show databases')
    print(cursor.fetchall())
except mysql.Error as err:
    print("failed to create db:{}",format(err))
conn.close()
