import sys 
from numpy import* 
r1, c1 = [int(a) for a in input("First matrix rows, cols: ").split()] 
r2, c2 = [int(a) for a in input("Second matrix rows, cols: ").split()] 

if c1!=r2: 
  print('Multiplication is not possible') 
  sys.exit() 

str1 = input('Enter first matrix elements:\n')
x = reshape(matrix(str1), (r1, c1)) 
str2 = input('Enter second matrix elements:\n') 
y = reshape(matrix(str2), (r2, c2)) 
print('The product matrix:') 
z = x * y 
print(z)
