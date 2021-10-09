try:
    x = int(input("Enter a number greater than zero :"))
    assert x > 0
    print(f"you entered {x}")
except:
    print("Wrong input entered")
