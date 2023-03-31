# 33 -

operacao = int(input('''Qual operação você deseja realizar? Sendo elas:
1 = Par ou Impar;
2 = Positivo ou negativo;
3 = Inteiro ou Decimal.
>>> '''))

n1 = float(input("Digite o primeiro número:\n"))
n2 = float(input("Digite o segundo número:\n"))
soma = n1 + n2

if operacao == 1:
    if soma % 2 == 0:
        print("Número é par.")
    else: print("Número é ímpar.")

elif operacao == 2:
    if soma >= 0:
        print("Número é positivo.")
    else: print("O número é negativo.")

elif operacao == 3:
    if soma == round(soma):
        print("Número é inteiro.")
    else:
        print("Número é decimal.")