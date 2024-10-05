# Aluno: Riquelmy Henrique Silva
# Curso: Ciência de Dados - Fatec Jundiaí
# Trabalho 1: Matrizes Triângulares

A = []
Asup = []
Ainf = []

i = 5

for m in range(0, i):

    matriz_linha = []

    for n in range(0, i):

        number = int(input(f"a{m+1}{n+1}: "))

        matriz_linha.append(number)

    A.append(matriz_linha)
    Asup.append(matriz_linha.copy())
    Ainf.append(matriz_linha.copy())


def desenhar_matriz(matriz):
    desenho = ""
    for m in range(0, i):
        for n in range(0, i):
            desenho += f"  {matriz[m][n]}"
        desenho += "\n"
    return desenho


for m in range(0, i):
    for n in range(0, i):
        if m > n:
            Asup[m][n] = 0

for m in range(0, i):
    for n in range(0, i):
        if n > m:
            Ainf[m][n] = 0

print(desenhar_matriz(A))
print(desenhar_matriz(Asup))
print(desenhar_matriz(Ainf))
