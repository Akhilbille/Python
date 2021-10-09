from random import *
secnum=randint(1,50)
print("Currently i'm thinking of a Number between 1 to 50")
print("Try to guess the secret number in 5 Chances")
count=0
for i in range(5):
    count+=1
    guess=int(input('Guess the Secret Number: '))
    if guess>secnum:
        print('Your Guess is High')
    elif guess<secnum:
        print('Your Guess is Low')
    else:
        break

if guess==secnum:
    print('Congratulations...! You have Guessed the Number :-)in %d chances' %count)
else:
    print('Better Luck Next Time :-(. Secret Number is ',secnum)
