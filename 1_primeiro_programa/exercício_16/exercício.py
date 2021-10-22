salário = float(input("Qual foi o seu salário? R$ "))

print(salário)

porcentagem_aumento = float(input("Digite a porcentagem de aumento desejada: "))

aumento = porcentagem_aumento * salário / 100 + salário

print(aumento)

novo_salario = aumento

print("Seu novo salário será de R$ %.2f" % novo_salario)