# 35 - 

tipocarne = input("Escolha o tipo de carne que deseja, sendo eles: File Duplo, Alcatra ou Picanha:\n").upper()
cartao = input("Você deseja utilizar o cartão Tabajara na sua compra?\n")

if tipocarne == "FILE DUPLO":
    if cartao == "sim" or cartao == "Sim" or cartao == "SIM":
        quantidade = int(input("Quantos Kg deseja comprar?\n"))
        if quantidade <= 5:
            precocarne = quantidade*34.90
            desconto = precocarne*0.05
            valor = precocarne - desconto
        elif quantidade > 5:
            precocarne = quantidade*35.80
            desconto = precocarne*0.05
            valor = precocarne - desconto

elif cartao == "nao" or cartao == "não" or cartao == "Não" or cartao == "NAO" or cartao == "NÃO":
    quantidade = int(input("Quantos Kg deseja comprar?\n"))
    if quantidade <= 5:
            precocarne = quantidade*34.90
            valor = precocarne
    elif quantidade > 5:
            precocarne = quantidade*35.80
            valor = precocarne

if tipocarne == "ALCATRA":
    if cartao == "sim" or cartao == "Sim" or cartao == "SIM":
        quantidade = int(input("Quantos Kg deseja comprar?\n"))
        if quantidade <= 5:
            precocarne = quantidade*44.90
            desconto = precocarne*0.05
            valor = precocarne - desconto
        elif quantidade > 5:
            precocarne = quantidade*46.80
            desconto = precocarne*0.05
            valor = precocarne - desconto

elif cartao == "nao" or cartao == "não" or cartao == "Não" or cartao == "NAO" or cartao == "NÃO":
    quantidade = int(input("Quantos Kg deseja comprar?\n"))
    if quantidade <= 5:
            precocarne = quantidade*44.90
            valor = precocarne
    elif quantidade > 5:
            precocarne = quantidade*46.80
            valor = precocarne

if tipocarne == "PICANHA":
    if cartao == "sim" or cartao == "Sim" or cartao == "SIM":
        quantidade = int(input("Quantos Kg deseja comprar?\n"))
        if quantidade <= 5:
            precocarne = quantidade*66.90
            desconto = precocarne*0.05
            valor = precocarne - desconto
        elif quantidade > 5:
            precocarne = quantidade*67.80
            desconto = precocarne*0.05
            valor = precocarne - desconto

elif cartao == "nao" or cartao == "não" or cartao == "Não" or cartao == "NAO" or cartao == "NÃO":
    quantidade = int(input("Quantos Kg deseja comprar?\n"))
    if quantidade <= 5:
            precocarne = quantidade*66.90
            valor = precocarne
    elif quantidade > 5:
            precocarne = quantidade*67.80
            valor = precocarne

print(f'''
Tipo da carne: {tipocarne};
Quantidade: {quantidade:.2f}Kg;
Preço total: R${precocarne:.2f};
Usou cartão: {cartao};
Desconto: {desconto:.2f}%
Valor a pagar: R${valor:.2f}''')