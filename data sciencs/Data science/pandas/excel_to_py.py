from pandas import *
df=read_excel("excel sheet path ")#df is a data frame we are compressing rows and colums into a single data frame object
df=read_csv("path of a csv file ")
# from dictionaries to dictionary data frame
emp={"emp":[1,2,3,]}
ddf=DataFrame((emp))
#for list of tuples to a data frame 
empdata=[(1001,"akhil",10000.00,"10-10-2020")]
dflt=DataFrame(empdata,columns=["E.no","Ename","sal","date_of_joining"])
df.shape#returns(number of rows , columns)
df.head()#returns us top 5 values
df.head(2)#returns upto top 2 values
df.tail()# returns last 5 values
df.tail(2)#returns last 2 values
df[4:6]#we used slicing to get middle values
# to get specific column details 
df["Ename"]#for single column data
dflt[["Ename,"sal"]]
dflt["sal"].max()
dflt.["sal"].min()
dflt.set_index(inplace=True)#for making empid as index 
dflt.loc[1004]#returns all details of a empid 1004
dflt.reset_index(inplae=True)#to reset index values
 

