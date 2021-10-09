amt=int(input("Enter Amount: "))
t=amt//2000
amt=amt%2000

f=amt//500
amt=amt%500

th=amt//200
amt=amt%200

h=amt//100
amt=amt%100

print("No of Notes: ", t+f+th+h)
print("2000's : ", t)
print("500's : ", f)
print("200's : ", th)
print("100's : ", h)