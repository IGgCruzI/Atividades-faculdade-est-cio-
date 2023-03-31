# 11 - Faça um algoritmo que o usuário possa digitar o seu nome e a sua idade. Utilizando a tabela abaixo, verifique em qual item se enquadra a idade da pessoa e escreva a mensagem: (nome) está com (idade) e pela tabela é considerado um (tipo)
nome = input("Qual seu nome? \n")

idade = int(input("Qual sua idade?\n"))

if idade > 0 and idade < 2:
    print("Bebê\n")
    tipo = 'Bebê'

elif idade > 3 and idade < 11:
    print("Criança\n")
    tipo = 'Criança'

elif idade > 12 and idade < 21:
    print("Jovem\n")
    tipo = 'Jovem'

elif idade > 22 and idade < 64:
    print("Adulto\n")
    tipo = 'Adulto'

elif idade > 65 and idade < 100:
    print("Idoso\n")
    tipo = 'Idoso'

elif idade >= 101:
    print("Muito velhinho\n")
    tipo = 'Muito velhinho'

print(f"{nome} está com {idade} anos e pela tabela é considerado um {tipo}.")