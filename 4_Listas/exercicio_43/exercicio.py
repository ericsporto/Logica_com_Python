itens = ["Bota", "Piano", "Livro", "Chaves"]

iten1 = input("Digite o item para procurarmos primeiro: ")
iten2 = input("Digite o segundo item a ser procurado: ")

i = 0

while i < len(itens):
    if itens[i] == iten1:
        print("O primeiro objeto foi encontrado antes! %s " % iten1)
        break
    
    elif itens[i] == iten2:
        print("O segundo objeto foi encontrado antes! %s " % iten2)
        break

    else:
        print("Não encontramos o seu Item!")
        break

    i = i + 1


