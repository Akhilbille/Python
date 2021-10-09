try:
    num=int(input("ENter a  number  : "))
    assert num>0, "Enter number above zero"
    print("It is a positive number")
except AssertionError:
    print("Its an Error :Enter number above Zero")