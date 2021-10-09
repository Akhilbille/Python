from abc import * 
class Car(ABC): 
   def __init__(self, regno): 
      self.regno = regno 
   def openTank(self): 
      print('Fill the fuel into the tank') 
      print('for the car with regno', self.regno) 
   @abstractmethod 
   def steering(self): 
      pass 
   @abstractmethod 
   def braking(self):
      pass
