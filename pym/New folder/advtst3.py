import mysql.connector as mys
myconn=mys.connect(host="localhost",user="root",password="@khilgowd143",database="dba")
cur=myconn.cursor()
try:
 cur.execute("select * from student")
 result=cur.fetchall()
 for i in result:
  print(i)
except:
 myconn.rollback()
myconn.close()