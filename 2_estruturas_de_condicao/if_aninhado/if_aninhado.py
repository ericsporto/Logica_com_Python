idade = int(input("Qual a sua idade?"))

if idade >= 18:
    print("Você pode entrar na balada.")

    pagamento = input("Forma de pagamento?")

    if pagamento == "dinheiro":
        print("A fila para dinheiro é a número 1. Obrigado")
    else:
        print("A fila para o cartão é a número 2. Obrigado")

else:
    print("Você não pode entrar na balada")