class team():
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.loses = 0
        self.draws = 0
        self.goal_difference = 0
        self.score = 0
    def Game(self,gd):
        self.goal_difference += gd
        if gd > 0 :
            self.wins += 1
            self.score += 3
        elif gd == 0:
            self.draws += 1
            self.score += 1
        elif gd < 0 :
            self.loses += 1
iran = team('Iran')
morocco = team('Morocco')
spain = team('Spain')
portugal = team('Portugal')

R1 = input()
x = int(R1[0])
y = int(R1[2])
iran.Game(x-y)
spain.Game(y-x)

R2 = input()
x = int(R2[0])
y = int(R2[2])
iran.Game(x-y)
portugal.Game(y-x)

R3 = input()
x = int(R3[0])
y = int(R3[2])
iran.Game(x-y)
morocco.Game(y-x)

R4 = input()
x = int(R4[0])
y = int(R4[2])
spain.Game(x-y)
portugal.Game(y-x)

R5 = input()
x = int(R5[0])
y = int(R5[2])
spain.Game(x-y)
morocco.Game(y-x)

R6 = input()
x = int(R6[0])
y = int(R6[2])
portugal.Game(x-y)
morocco.Game(y-x)

li = [[iran, iran.name, iran.wins, iran.score], [portugal, portugal.name, portugal.wins, portugal.score], [spain, spain.name, spain.wins, spain.score], [morocco, morocco.name, morocco.wins, morocco.score]]

li.sort(key=lambda x: x[1])
li.sort(key=lambda x: -x[2])
li.sort(key=lambda x: -x[3])

a = li[0][0]
b = li[1][0]
c = li[2][0]
d = li[3][0]

for i in (a, b, c, d):
    print('%s  wins:%i , loses:%i , draws:%i , goal difference:%i , points:%i' % (i.name, i.wins, i.loses, i.draws, int(i.goal_difference), i.score))