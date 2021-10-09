
import matplotlib.pyplot as plt 

slices = [50, 20, 15, 15] 
depts = ['Sales', 'Production', 'HR', 'Finance'] 
cols = ['magenta', 'cyan', 'brown', 'gold'] 

plt.pie(slices, labels=depts, colors=cols, startangle=90, explode=(0, 0, 0.2, 0), shadow=True, autopct='%.1f%%')

plt.title('WIPRO') 

plt.legend() 
plt.show()
