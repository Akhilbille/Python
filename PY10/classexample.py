class Student: 
   def __init__(self): 
      self.name = 'Ram'
      self.age = 20  
      self.marks = 900 
   def talk(self): 
      print('Hi, I am ', self.name) 
      print('My age is', self.age) 
      print('My marks are', self.marks)

tarun=Student()
tarun.talk()
