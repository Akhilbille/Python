import math 
class Square: 
   def area(self, x): 
      print('Square area= %.4f'% x*x) 

class Circle(Square): 
   def area(self, x): 
      print('Circle area= %.4f'% (math.pi*x*x)) 

c = Circle() 
c.area(15)
