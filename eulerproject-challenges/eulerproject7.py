import math

def is_prime(n):
    m = int(math.sqrt(n))+1
    for i in range(2,m):
        if n % i == 0 :
            return False
    return True

j = 1
i = 2
l = 0
while j <= 10001:
    if is_prime(i):
        l = i
        j += 1
    i += 1
print(l)