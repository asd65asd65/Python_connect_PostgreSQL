# -*- coding: utf-8 -*-
"""
import

"""
import psycopg2
"""
funtion

"""
def show():
    #connect database
    conn = psycopg2.connect(database="testdb", user="postgres", password="er6319", 
                            host="127.0.0.1", port="5432")
    
    print("Opened database successfully")
    
    cur = conn.cursor()
    #Query all
    cur.execute("select * " +
                "from prevent_disease " +
                "order by id ")
    column = ["Id", "Name", "Temperature", "Getmask", "Date"]
    #data
    rows = cur.fetchall()
    #data output
    for row in rows:
        for i in range(5):
            print(column[i], "=", row[i])
        print("")
    total = cur.rowcount
    print("查詢結果:", total, "筆資料")
    print("")
    conn.close()
"""
main

"""
show()