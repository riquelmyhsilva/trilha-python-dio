a = [[4, 2]]

b = [[2], [3]]

c = [[]]


def multiplicar_matrizes(a, b):
    i = 0
    while i < len(a):
        j = 0
        while j < len(b):
            value = (a[i][j] * b[j][i]) + (a[j][i] * b[i][j])
            c[i].append(value)
            j += 1
        i += 1


multiplicar_matrizes(a, b)
print(c)


def mb(a, b):
    for i in range(len(a)):
        pass
