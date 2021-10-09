import mysql.connector
myconn=mysql.connector.connect(host = "localhost", user= "root", password = "",database="company")
cur=myconn.cursor()#to create cursor for we use for writing queries

# we use exception handling for handling errors in our connection
try:
    dbs=cur.execute("CREATE TABLE employee(emp_id INT,first_name VARCHAR(50),last_name VARCHAR(50),birth_date YEAR,gender char(1),salary INT,super_id INT,branch_id INT)") # we write queries with in the quotes
    cur.commit()
    
except:
    myconn.rollback()
finally: 
    myconn.close() # to close the database