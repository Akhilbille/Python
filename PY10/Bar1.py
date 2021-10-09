import matplotlib.pyplot as plt
from pandas import *
df=read_csv('E:\Python\pygraph\swin.csv')


plt.plot(df['Output Power'], df['Efficiency'],label='Output Power vs Efficiency', color= 'red') 

#set title and labels 
plt.title('Swinburne\'s Test') 
plt.xlabel('Output Power in kw') 
plt.ylabel('Efiiciency in %') 

plt.legend()
#show the line chart 

plt.show()
