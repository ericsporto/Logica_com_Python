lista = []

i = 0

while i <= 10:
    lista.append(i)
    i = i + 1

print(lista)

j = 0

while j < len(lista):
    if lista[j] == 4:
        del lista[j]
    j = j + 1

print(lista)


lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

k = 0

while k < len(lista1):
    if lista1[k] == 7:
        del lista1[k]
    k = k + 1

print(lista1)
