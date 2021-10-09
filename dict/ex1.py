players={}
for i in range(int(input("enter number of players in a match : "))):
    name=input("Enter player name : ")
    score=int(input("Enter score : "))
    players.update({name:score})
for pname in players.keys():
    print(pname)
name=input("Enter player name : ")
runs=players.get(name,-1)
if runs==-1:
    print("PLayer not Found")
else:
    print("Player name : {}  \nRuns : {} ".format(name,runs))