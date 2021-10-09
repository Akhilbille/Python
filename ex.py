class ra(Exception):
 def _init_ (self,arg):
  self.msg=arg
class mu(Exception):
 def_init_(self,arg):
  self.msg=arg
try:
 am=int(input("enter amount : "))
 if(100<am>15000):
  raise ra("enter amount in range of 100 to 15000")
 elif(am%100!==0):
else:
 print("your amout %d  is debited"%d)
except ra as r:
 print(r)
except mu as m:
 print(m)
  