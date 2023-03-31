# 9 - Faça um algoritmo que leia o nome de um aluno, o nome da disciplina, nota de 3 provas e calcule a média desse aluno e verifique se o aluno foi aprovado. Sabendo que para ser aprovado a média deverá ser maior ou igual a 6,0.
print("Seja bem vindo ao sistema de médias do ALUNO.\n")

nome = input("Olá, como devemos lhe chamar?\n")

disciplina = input(f"{nome}, para prosseguirmos, nos informe a matéria que deseja verificar a média?\n")

n1 = int(input("Informe sua primeira nota:\n"))
n2 = int(input("Informe sua segunda nota:\n"))
n3 = int(input("Informe sua terceira nota: \n"))

media = (n1+n2+n3)/3

if media >= 6:
    print(f"Parabéns {nome}, você foi aprovado!\n")

elif media < 6:
    print(f"{nome}, infelizmente você foi reprovado!")

print(f'''Vou lhe informar o que você nos forneceu:

Nome: {nome};
Disciplina: {disciplina}
Primeira nota: {n1};
Segunda nota: {n2};
Terceira nota: {n3};
Média final: {media} e você foi APROVADO!.''')