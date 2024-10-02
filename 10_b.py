#Design a database application to search the specified record from the database. 

import mysql.connector as mysql
conn=mysql.connect(user='root',password='vivek@12345',host="localhost")
cursor=conn.cursor()

cursor.execute("USE Ahamed")
cursor.execute("CREATE TABLE EMP(EMPID INT NOT NULL,ENAME VARCHAR(25)NOT NULL,SAl INT NOT NULL,PRIMARY KEY(EMPID)) ENGINE=InnoDB")
cursor.execute("show tables from Ahamed")
print(cursor.fetchall())
conn.close()