import math

from typing import Counter
def is_prime(n):
    m = int(math.sqrt(n))+1
    for i in range(2,m):
        if n % i == 0 :
            return False
    return True

def a(n):
    for i in range(n):
        x = [i for i in range(1,n+1) if not n % i]
        return(x)

l = []
d = {}
counter = 0

for i in range(0,10):
    l.append(int(input()))
l.sort()
for i in l:
    m = a(i) #m : مقسوم علیه های این مقدار
    m.remove(1)
    for n in m:
        if is_prime(n):
            counter += 1
    d[counter]= i
    counter = 0

max_key = max(d.keys())
print(d[max_key],max_key)