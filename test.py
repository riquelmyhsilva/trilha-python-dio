A = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

I = []

n = 6
n2 = 5

for p in range(0, n):
    i = []
    for k in range(0, n2):
        if p == k:
            i.append(1)
        else:
            i.append(0)

    I.append(i)

print(I)
