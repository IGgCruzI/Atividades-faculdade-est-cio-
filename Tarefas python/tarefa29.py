# 29 -
altura = float(input("Informe sua altura:\n"))
sexo = input("Você é homem ou mulher?\n")

if sexo == "homem":
    pesoideal = (72.7*altura)-58

else: pesoideal = (62.1*altura)-44.7

print(f"Seu peso ideal é de {pesoideal}.")