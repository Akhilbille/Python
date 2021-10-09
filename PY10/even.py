p,che,b,m,cs=[int(i) for i in input('Enter 5 values: ').split()]
Percentage=((p+che+b+m+cs)/500)*100
print('Percentage : ',Percentage)
if Percentage >= 90 :  
    print('Grade A')
elif Percentage >= 80: 
    print('Grade B')
elif Percentage >= 70: 
    print('Grade C')
elif Percentage >= 60: 
   print('Grade D')
elif Percentage >= 40: 
    print('Grade E')
elif Percentage < 40: 
    print('Grade F')
