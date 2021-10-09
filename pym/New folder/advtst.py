try:
 a=int(input("enter the numerator:"))
 b=int(input("enter the denominator"))
 c=a/b
 print(c)
except ZeroDivisionError:
 print("dont enter zero in denominator choose any other positive integer")
finally:
 print("close file")