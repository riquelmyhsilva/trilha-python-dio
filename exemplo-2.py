A = []
B = []

i = 3
j = 2

for m in range(0, i):
    mtz = []
    mtz_inv = []
    for n in range(0, j):
        number = int(input(f"a{m+1}{n+1}: "))
        mtz.append(number)
        mtz_inv.append(-number)

    A.append(mtz)
    B.append(mtz_inv)

print(A)
print("--------------------")
print(B)
