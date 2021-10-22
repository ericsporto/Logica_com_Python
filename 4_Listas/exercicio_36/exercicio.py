notas = [10, 8, 10, 9, 5]

i = 0
soma_notas = 0

while i < 5:
    soma_notas = soma_notas + notas[i]
    i = i + 1

media = soma_notas / 5

print("A média das notas é: %.1f" % media)