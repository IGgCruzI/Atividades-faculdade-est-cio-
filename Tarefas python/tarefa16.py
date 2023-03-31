# 16 - Faça um Programa que leia três números e mostre o maior e o menor deles.
n1 = int(input("Digite o primeiro número:\n"))
n2 = int(input("Digite o segundo número:\n"))
n3 = int(input("Digite o terceiro e último número:\n"))

numeros = [n1,n2,n3]

maior_valor = max(numeros)
menor_valor = min(numeros)

print("O maior número é", maior_valor)
print("O menor número é", menor_valor)