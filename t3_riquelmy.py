# Aluno: Riquelmy Henrique Silva
# Curso: Ciência de Dados - Fatec Jundiaí
# Trabalho 3: Multiplicação de Matrizes

a = [[5, 5, 6], [3, 2, 8], [5, 7, 7]]

b = [[5, 5, 9], [1, 2, 8], [5, 8, 7]]

c = [[], [], []]


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
