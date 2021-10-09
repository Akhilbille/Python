amount = int(input('Enter Amount to Draw :'))
if(amount%5 == 0):
  dem=[{2000:''},{500:''},{200:''},{100:''},{50:''},{20:''},{10:''},{5:''}]
  totalNotes = 0;
  for i in range(0,len(dem)):
    key=dem[i].keys()[0]
    value = amount//key
    amount %= key
    dem[i][key ] = value
    totalNotes +=value
  print ('Total denomination :',dem, '\n' ,'Total Notes : ',totalNotes)
else:
  print('Please Enter Valid Amount')
