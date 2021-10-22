lista = ["Pão", "manteiga", "mel", "patê"]

i = 0

item_procurado = input("O que deseja procurar? ")

achou = False

while i < len(lista):
    if lista[i] == item_procurado:
        print("Encontramos o item %s" % item_procurado)
        achou = True
    i = i + 1

if achou == False:
    print("NÃo encontramos o item %s procurado" % item_procurado)
    
    


