# Aluno: Riquelmy Henrique Silva
# Curso: Ciência de Dados - Fatec Jundiaí
# Trabalho 2: Soma de Matrizes

A = []
B = []
C = []

Am = int(input("Defina o comprimento da matriz A: "))
An = int(input("Defina a altura da matriz A: "))
Bm = int(input("Defina o comprimento da matriz B: "))
Bn = int(input("Defina o altura da matriz B: "))


def somar_matrizes(matriz_1, matriz_2):
    matriz_somada = []
    for i in range(0, An):
        matriz_linha = []
        for j in range(0, Am):
            number = matriz_1[i][j] + matriz_2[i][j]
            matriz_linha.append(number)
        matriz_somada.append(matriz_linha)
    return matriz_somada


def desenhar_matriz(matriz):
    desenho = ""
    for i in range(0, An):
        for j in range(0, Am):
            desenho += f"  {matriz[i][j]}"
        desenho += "\n"
    return desenho


if Am == Bm and An == Bn:
    for i in range(0, An):
        matriz_linha_a = []
        for j in range(0, Am):
            number = int(input(f"a{i+1}{j+1}: "))
            matriz_linha_a.append(number)
        A.append(matriz_linha_a)
    for i in range(0, Bn):
        matriz_linha_b = []
        for j in range(0, Bm):
            number = int(input(f"b{i+1}{j+1}: "))
            matriz_linha_b.append(number)
        B.append(matriz_linha_b)
    C = somar_matrizes(A, B)
    print(desenhar_matriz(A))
    print(desenhar_matriz(B))
    print(desenhar_matriz(C))
else:
    print("Impossível somar.")
