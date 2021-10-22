numero = int(input("Digite o número: "))

divisoes = 0

contador = numero

while contador > 0:

    if numero % contador == 0:
        divisoes = divisoes + 1
        
    contador = contador - 1


if divisoes == 2:
    print("o numero %d é primo!" % numero)
else:
    print("o numero %d Não é primo" % numero)
