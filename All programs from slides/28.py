num = int(input("Enter a number to find prime number s till that  number : "))
for i in range(2, num + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end=" ")
