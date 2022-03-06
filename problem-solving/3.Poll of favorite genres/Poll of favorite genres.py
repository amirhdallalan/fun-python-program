poll = {'Horror' : 0, 'Romance' : 0, 'Comedy' : 0, 'History' : 0 , 'Adventure' : 0 , 'Action': 0}
num = int(input())
for i in range(0,num):
    nazar = input().split(" ")
    for j in nazar:
        if j in poll:
            poll[j] += 1
l = list()
for k in list(poll.keys()):
    l.append([k, -poll[k]])
l.sort()
l.sort(key = lambda x: x[1])
for i in l:
    print(i[0],':',-i[1])