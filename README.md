# Python_connect_PostgreSQL
利用 python 與 PostgreSQL 資料庫互動

<h2>開發環境:</h2>
套件管理器: anaconda 3</br>
程式語言: python 3.7.3</br>
<h4>需要的套件: </h4>
<ul>
<li>psycopg2</li>
</ul>

<h4>需要的軟體: </h4>
<ul>
<li>PostgreSQL 12.2</li>
</ul>

<h2>連接到資料庫:</h2>
<div>
  import psycopg2</br></br>
  #與資料庫建立連線</br>
  conn = psycopg2.connect(database="testdb", user="postgres", password="pass123", host="127.0.0.1", port="5432")</br></br>

  cur = conn.cursor()</br>
  #向資料庫輸入指令</br>
  cur.execute( "Query 指令" )</br></br>
</div>
