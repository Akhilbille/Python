












import mysql.connector  
myconn = mysql.connector.connect(host = "localhost", user = "root",password = "naveen",database="abd")   
cur = myconn.cursor()  

try:  
    cur.execute("delete from Employee where id = 110")  
    myconn.commit()
except:  
    myconn.rollback()    

myconn.close() 

