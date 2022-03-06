from random import choice

class Human():
    def __init__(self, name):
        self.name = name

class Player(Human):
    count = 22 #تعداد بازیکنان بدون تیم
    num = {'A': 0, 'B': 0} #دیکشنری جهت شمارش تعداد اعضای هر تیم
    def team_chooser(self): #متد تعیین تیم
        Player.count -= 1
        if Player.num['A'] < 11 and Player.num['B'] < 11: # تعیین تیم تا هنگامی که هر دو تیم جای خالی دارند
            x = choice(['A','B'])
            self.team = x
            Player.num[x] += 1
        elif Player.num['A'] == 11: #تعیین تیم هنگامی که تیم آ پر می شود
            self.team = 'B'
        elif Player.num['B'] == 11: #تعیین تیم هنگامی هنگامی که تیم ب پر می شود
            self.team = 'A'

names = ['hosein', 'maziar', 'akbar', 'nima', 'mahdi', 'farhad', 'mohammad', 'khashayar', 'milad', 'mostafa', 'amin', 'saeid', 'pooya', 'poorya', 'reza', 'ali', 'behzad', 'soheil', 'behrooz', 'shahrooz', 'saman', 'mohsen']

for name in names:
    name = Player(name)
    name.team_chooser()
    print (name.name,name.team)