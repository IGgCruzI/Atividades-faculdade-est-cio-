# 13 - Faça um algoritmo que leia o número digitado e verifique se é par ou ímpar
numero = int(input("Digite um número:\n"))

if (numero%2) == 0:
    print(f"O número {numero} é par.\n")

else: print(f"O número {numero} é ímpar.\n")