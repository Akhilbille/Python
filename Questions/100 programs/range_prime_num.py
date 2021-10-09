def prime_num(start, stop):
    if start > 1:
        for j in range(start, stop + 1):
            for i in range(2, j):
                if j % i == 0:
                    break

            else:
                print(j, end=" ")


prime_num(int(input("enter strating  number : ")), int(input("enter ending number : ")))
