def f(n): 
   if n==0 or n==1: 
      return 1 
   else: 
      return n*f(n-1) 


for i in range(1,11):
   print("Factorial of %d is %d " %(i,f(i)))
