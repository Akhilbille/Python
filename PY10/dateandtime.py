from datetime import *
from calendar import *
  
date = input('Enter Date in dd - mm- yyyy format: ')
born = datetime.strptime(date, '%d-%m-%Y').weekday() 

print(day_name[born]) 
