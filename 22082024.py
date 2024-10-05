import random

a = [1, 2, 3, 4, 5, 6]
b = [num**3 for num in a if num % 2 != 0]
print(b)
num = 2
lista = []
while True:
    x = [random.randint(1, 10000) for _ in range(1)]
    lista.append(x)
    lista.sort()
    print(lista)
