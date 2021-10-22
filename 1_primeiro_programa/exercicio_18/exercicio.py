saldo = 359.56

print("Seu saldo é R$%s" % saldo)

nova_quantia = float(input("Digite a nova quantia: "))

soma = saldo + nova_quantia - 125.98

print("Seu saldo final menos R$125.98 de sua fatura é R$%.2f" % soma)