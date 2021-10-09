def prime_num(num):

    for i in range(2, num):
        if num % i == 0:
            print("NOt a prime number ")
            break
    else:
        print("It is a prime number ")


prime_num(int(input("enter a number : ")))
