class Player:
    def __init__(self,matches,goals,rating,name):
        self.matches=matches
        self.goals=goals
        self.ratings=rating
        self.name=name
class FootballLeague:
    def __init__(self,League,playerlist):
        self.League=League
        self.playerlist=playerlist
    def playerbyrating(self):
        rating=[]
        for i in self.playerlist:
            rating.append(i.ratings)
            max_r=max(rating)
        for j in self.playerlist:
            if max_r==j.ratings:
                print(j.matches)
                print(j.goals)
                print(j.ratings)
                print(j.name)
                return True
    def playerbygoal(self):
                goal=[]
                for i in self.playerlist:
                    print(i)
                    goal.append(i.goals)
                goal.sort()
                for j in goal:
                    print(j)

num = int(input())
myleague=[]
for i in range(num):
    match=int(input())
    goal=int(input())
    rating=int(input())
    name=input()
myleague.append(Player(match,goal,rating,name))

fleague = FootballLeague('Fifa',myleague)
fleague.playerbyrating()
fleague.playerbygoal()
