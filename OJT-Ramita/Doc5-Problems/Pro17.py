'''17.Create a function that takes the number of wins, draws and losses and calculates 
the number of points obtained so far for 'n' number of football teams . Print the winner 
team in the end .
wins get +3 points, draws get +1 point, losses get -1 points .

I/p:
Team1(3, 4, 2) ## calculation : 3*3 +4*1 + 2(-1) = 11

Team2(5, 0, 2) ## calculation : 5*3 + 0*1 + 2(-1) = 13
Team3(0, 0, 1) ## calculation : 0*3 + 0*1 + 1(-1) = -1

O/p:
Winner: Team2'''


Data = {"team1":(3,4,2), "team2":(5,0,2), "team3":(0,0,1)}
score = 0
team = ""

for i in Data:
    temp = (Data[i][0]*3)+(Data[i][1]*1)+(Data[i][2]*(-1))
    if temp > score:
        score = temp
        team = i
print("Winner:",team)
    