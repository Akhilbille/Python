from sys import *

while(True):
    print('1. Addittion')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Exponent')
    print('6. Modulo Division')
    print('7. Integer Division')
    print('8. Exit')
    choice=int(input('Choose a number between 1 to 8: '))
    if choice==8:
        exit()
    if 1<=choice<=7:
        a=int(input('Enter a Value: '))
        b=int(input('Enter b Value: '))
        if choice==1:
            print('Sum : ',a+b)
        elif choice == 2:
            print('Difference : ',a-b)
        elif choice ==3:
            print('Multiplication : ',a*b)
        elif choice ==4:
            print('Division : ',a/b)
        elif choice ==5:
            print('Exponent : ',a**b)
        elif choice ==6:
            print('Modulo Divison : ',a%b)
        elif choice ==7:
            print('Integer Divison : ',a//b)
            
    else:
        print('Please Enter a number between 1 to 8')
