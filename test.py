# -*- coding: utf-8 -*-

"""
import

"""
import psycopg2
import matplotlib.pyplot as plt
import numpy as np
"""
funtion

"""
def show():
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
    return cur.rowcount
def showFever():
    #Query temperature >= 38
    cur.execute("select * " + 
                "from prevent_disease " + 
                "where temperature >= 38 " + 
                "order by id ")
    return cur.rowcount
def showNotGetMask():
    #Query not getmask
    cur.execute("select * " + 
                "from prevent_disease " + 
                "where getmask = false " + 
                "order by id ")
    return cur.rowcount
def showBarPlots(labels, ratings, ylabel, title):
    index = np.arange(len(labels))
    plt.bar(index, ratings)
    plt.xticks(index, labels)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()
#connect database
conn = psycopg2.connect(database="testdb", user="postgres", password="er6319", 
                        host="127.0.0.1", port="5432")

print("Opened database successfully")

cur = conn.cursor()
total = show()
print("查詢結果:", total, "筆資料")
print("")

fever = showFever()
print("體溫過高人數:", fever)
labels = ["Normal", "Fever"]
ratings = [total-fever, fever]
showBarPlots(labels, ratings, "Temperature", "Temperature Statistics")
print("")

noMask = showNotGetMask()
print("未領取口罩人數:", noMask)
labels = ["Get", "Not Get"]
ratings = [total-noMask, noMask]
showBarPlots(labels, ratings, "People", "GetMask Statistics")
print("")

conn.close()