Lista = [1, 7, 70, 46, 23]

procuro = int(input("Qual numero deseja procurar? "))

encontrado = False

for n in Lista:
    if n == procuro:
        print("O número %d foi encontrado!" % procuro)
        encontrado = True

if encontrado == False:
    print("NÃo encontramos o seu número!")
    
    