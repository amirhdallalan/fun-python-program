def sum_square(n):
    sq = 0
    for i in range(1,n+1):
        sq += i**2
    return sq

def square_sum(n):
    qs = 0
    for i in range(1,n+1):
        qs += i
    qs **= 2
    return qs

x = square_sum(100)-sum_square(100)
print(x)