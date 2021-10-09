colors = {'r': "Red", 'g': "Green", 'b': "Blue", 'w': "White"}
for k in colors: 
   print (k)
print('---------------')

for k in colors: 
   print (colors[k])

print('---------------')

for k, v in colors.items(): 
   print('Key= {} Value= {}'. format(k, v))
