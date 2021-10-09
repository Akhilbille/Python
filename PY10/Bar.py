import matplotlib.pyplot as plt
from pandas import *

empdata={"EmpId":[1001,1002,1003,1004,1005,1006],"Ename":["Balu","Gautham","Gani","Siddarth","Subbu","Jai"],"Sal":[25000,36500,45200,32000,18500,26000],"DoJ":["30-6-2014","25-12-2016","24-5-2015","16-5-2013","22-11-2018","19-8-2012"]}

df = DataFrame(empdata) 

x = df['Ename'] 
y = df['Sal'] 

plt.bar(x,y, label='Employee data', color='#160c63') 

plt.xlabel("Employee ID's") 
plt.ylabel('Employee Salaries') 

plt.title('Digi Brains Academy') 
#show legend 
plt.legend() 
#display the graph 
plt.show()

