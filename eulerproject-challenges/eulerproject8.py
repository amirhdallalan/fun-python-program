
stats = {'a':1000, 'b':3000, 'c': 100}
m = max(stats.items(), key=operator.itemgetter(1))[0]
print(m)