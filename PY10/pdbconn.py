import mysql.connector  
myconn = mysql.connector.connect(host = "localhost", user = "root",password = "naveen",database = "ismart")  
cur = myconn.cursor()

try:  
    cur.execute("delete from teacher where id=103")  
    myconn.commit()
  
except:  
    myconn.rollback()  

myconn.close() 
