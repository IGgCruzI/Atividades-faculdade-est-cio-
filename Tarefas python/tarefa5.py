# 5 - Faça um algoritmo que leia o nome deo aluno, o nome da disciplina, notas de 3 provas e calcule a média do aluno. Posteriormente imprima o resultado de cada variável linha abaixo de linha.
print("Seja bem vindo ao Sistema de médias Estácio.\n")

nome = input("Para começarmos, nos diga seu nome.\n")

materia =input(f"{nome}, informe a matéria que você deseja descobrir a média.\n")

print(f"Certo {nome}, para descobrirmos sua média precisamos de suas 3 notas.\n")

m1 = int(input(f"{nome}, qual foi sua primeira média?\n"))
m2 = int(input("Segunda média?\n"))
m3 = int(input("Terceira média?\n"))

media = (m1+m2+m3)/3

print(f'''{nome}, suas notas foram as seguintes:

Primeira prova: {m1:.2f};

Segunda prova: {m2:.2f};

Terceira prova: {m3:.2f}

E sua média foi de {media}.''')
