from random import *
name=input("Your Name: ")
secnum=randint(1,10)
print("Hey %s... Currently i'm thinking of a number between 1 to 10" %name)
print("Try to guess the number...")
count=0


for i in range(1,4):
    guess=int(input("Your Guess...: "))   
    count+=1
    if guess<secnum:
       print("Your guess is Low")
    elif guess>secnum:
       print("Your guess is High")
    else:
       break

if guess==secnum:
    print("Congratulations %s....! you have guessed in %d guesses" %(name,count))
else:
    print("Better Luck Next Time %s :-(. Secret Number is %d"%(name,secnum))