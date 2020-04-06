# Python_connect_PostgreSQL
健康管理資料庫
<h2>需要:</h2>
<ul>
<li>安裝 PostgreSQL</li>
<li>安裝 psycopg2 套件</li>
</ul>
<h2>說明:</h2>
使用 psycopg2 套件</br>
import psycopg2</br></br>
與資料庫建立連線</br>
conn = psycopg2.connect(database="testdb", user="postgres", password="pass123", host="127.0.0.1", port="5432")</br></br>
向資料庫輸入指令</br>
cur.execute( "Query 指令" )</br></br>
