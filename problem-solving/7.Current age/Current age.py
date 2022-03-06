from datetime import date

def calculateAge(birthDate):
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age
bd = input().split("/")
y = int(bd[0])
m = int(bd[1])
d = int(bd[2])
if y > 2021:
    print('WRONG')
elif m > 12:
    print('WRONG')
elif d > 31:
    print('WRONG')
else:
    print(calculateAge(date(y,m,d)))