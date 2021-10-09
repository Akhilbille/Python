for row in range(0, 5):
    for spaces in range(5 - row):
        print(" ", end=" ")
    for symbol in range(1 + row):
        print("*", end=" ")
    print()
