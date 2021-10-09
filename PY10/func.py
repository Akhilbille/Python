def modify(lst): 
   lst = [10, 11, 12]
   print(lst, id(lst)) 


lst = [1,2,3,4] 
modify(lst) 
print(lst, id(lst))
