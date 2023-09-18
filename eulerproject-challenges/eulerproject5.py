i = 1
for n in range(1,21):
    if not i % n == 0:
        for a in range(1,21):
            k = i * a
            if k % n == 0:
                i = k
                break
print(i)