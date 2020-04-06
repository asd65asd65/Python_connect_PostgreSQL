# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 21:59:42 2020

"""

import psycopg2

#connect database
conn = psycopg2.connect(database="testdb", user="postgres", password="er6319", 
                        host="127.0.0.1", port="5432")

print("Opened database successfully")

cur = conn.cursor()

#Query all
cur.execute("select * " +
            "from prevent_disease " +
            "order by id ")

column = ["Id", "Name", "Temperature", "Getmask"]
#data
rows = cur.fetchall()
#data output
for row in rows:
    for i in range(4):
        print(column[i], "=", row[i])
    print("")
print("查詢結果:", cur.rowcount, "筆資料")
print("Operation done successfully")

#Query temperature >= 38
cur.execute("select * " + 
            "from prevent_disease " + 
            "where temperature >= 38 " + 
            "order by id ")
print("體溫過高人數:", cur.rowcount)

#Query not getmask
cur.execute("select * " + 
            "from prevent_disease " + 
            "where getmask = false " + 
            "order by id ")
print("未領取口罩人數:", cur.rowcount)
conn.close()