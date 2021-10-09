try:
  n=int(input("enter the numerator:"))
  d=int(input("enter the denominator:"))
  print(n/d) 
except ZeroDivisionError:
  print("dont enter zero in denominator enter any number greater than zero")
finally:
  print("file closed")