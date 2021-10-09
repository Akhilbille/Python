import mysql.connector  
myconn = mysql.connector.connect(host = "localhost", user = "root",password = "naveen",database = "ismart")  
cur = myconn.cursor()  

sql = "insert into Teacher(name, id, salary, dept_id, branch_name) values (%s, %s, %s, %s, %s)"  
val = ("Mike",105,28000,202,"Guyana")  
      
try:  
    cur.execute("select * from Teacher")  
    result = cur.fetchall()  
      
    for x in result:  
        print(x) 

  
except:  
    myconn.rollback()  

  
myconn.close()
