renda = float(input("Qual a sua renda? "))

print(renda)

if renda >= 0 and renda <= 2000:
    print("Você tem R$1000.00 de limite disponível")
elif renda >= 2000 and renda <= 4000:
    print("Você tem R$2000.00 de limite disponível")
elif renda >= 4000 and renda <= 6000:
    print("Você tem R$3000.00 de limite disponível")
elif renda >= 10000:
    print("Por favor, falar com o seu Gerente!")
