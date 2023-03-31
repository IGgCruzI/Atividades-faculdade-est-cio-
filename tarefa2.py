# 2 - Faça um algoritmo que leia o nome e as notas dos 4 bimestres de um aluno. Posteriormente imprima o resultado de cada variável linha abaixo de linha.
print("\nBem vindo ao sistema de verificação de média bimestral.\n")
nome = input("Para continuarmos, me informe seu nome:\n")
b1 = float(input(f"\nAntes de tudo {nome}, nos diga qual foi sua nota no primeiro bimestre:\n"))
if b1 < 6:
    print(f"{nome}, sua primeira nota está abaixo da média. \n")
elif b1 >= 6:
    print(f"{nome}, sua primeira nota está acima da média.\n")
b2 = float(input(f"{nome}, diga agora qual foi sua média no segundo bimestre:\n"))
if b2 < 6:
    print(f"{nome}, sua segunda nota está abaixo da média...\n")
elif b2 >= 6:
    print(f"{nome}, sua segunda nota está acima da média\n")
media1 = (b1+b2)/2
print(f"{nome}, sua média até agora é de {media1:.2f}\n")
b3 = float(input(f"{nome}, qual foi a sua nota no terceiro bimestre?\n"))
if b3 >= 6:
    print(f"{nome}, sua terceira nota foi acima da média\n")
elif b3 < 6:
    print(f"{nome}, sua terceira nota foi abaixo da média\n")
media2 = (b1+b2+b3)/3
print(f"{nome}, sua média até o momento é de {media2:.2f}, lembrando que a média final deve ser igual ou superior a 6. \n")
b4 = float(input(f"{nome}, para finalizarmos, qual a sua nota no quarto bimestre?\n"))
if b4 >= 6:
    print(f"{nome}, sua quarta nota foi acima da média \n")
elif b4 < 6:
    print(f"{nome}, sua quarta nota foi abaixo da média... \n")
media3 = (b1+b2+b3+b4)/4
if media3 >= 6:
    print(f"Parabéns {nome}, você está acima da média, sua nota é {media3:.2f}")
elif media3 < 6:
    print(f"Infelizmente {nome}, você está abaixo da média, sua nota é {media3:.2f}\n")
print(f'''{nome}, suas notas por bimestre foram:
1º Bimestre: {b1};
2º Bimestre: {b2};
3º Bimestre: {b3};
4º Bimestre: {b4}.''')