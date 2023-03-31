# 34 - 
combustivel = input("Qual combustível deseja utilizar para abastecer seu veículo?Sendo as opções sendo (A) para álcool ou (G) para gasolina:\n").upper()
precogasolina = 2.5
precoalcool = 1.9

if combustivel == "A":
    quantidade = int(input("Quantos litros deseja abastecer?\n"))
    if quantidade <=20:
        valor = (quantidade*precoalcool)
        desconto20 = (valor*0.03)
        valorfinal = (valor - desconto20)
    elif quantidade > 20:
        valor = (quantidade*precoalcool)
        desconto20mais = (valor*quantidade)*0.04
        valorfinal = (valor - desconto20mais)
    
elif combustivel == "G":
    quantidade = int(input("Quantos litros deseja abastecer?\n"))
    if quantidade <= 20:
        valor = (quantidade + precogasolina)
        desconto20 = (quantidade*0.04)
        valorfinal = (valor - desconto20)
    elif quantidade > 20:
        valor = (quantidade * precogasolina)
        desconto20mais = (quantidade*0.06)
        valorfinal = (valor - desconto20mais)

print(f'''
Valor a ser pago: R${valorfinal}''')
