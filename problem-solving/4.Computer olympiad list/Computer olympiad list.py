
num = int(input())
infos = []
for i in range(0,num):
    info = input().split(".")
    infos.append(info)

for user in infos:
    user[1] = user[1].capitalize()

infos.sort(key = lambda x : x[1])
infos.sort(key = lambda x : x[0], reverse=False)
print(infos)
