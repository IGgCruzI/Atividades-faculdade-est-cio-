# 1 - Faça um algoritmo que leia o nome, a idade, o sexo, o endereço e o telefone. Posteriormente imprima o resultado de cada variável linha abaixo de linha.

nome = input("Olá, como devemos lhe chamar?\n")

idade = int(input(f"Qual a sua idade {nome}?\n"))

sexo = input(f"{nome}, nos diga, você é um homem ou mulher?\n")

endereco = input(f"{nome}, caso precisemos te procurar, onde você mora?\n")

telefone = input(f"{nome}, e caso você não esteja, em qual número devemos ligar? \n")

print(f'''Certo {nome}, vamos confirmar as informações que nos passou:

Nome: {nome};
Idade: {idade};
Sexo: {sexo};
Endereço: {endereco};
Telefone: {telefone}.''')