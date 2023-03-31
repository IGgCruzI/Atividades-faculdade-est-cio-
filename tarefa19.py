# 19 - Faça um Programa que peça os 3 lados de um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

lado1 = int(input("Indique o tamanho do  primeiro lado do triângulo:\n"))
lado2 = int(input("Indique o tamanho do  segundo lado do triângulo:\n"))
lado3 = int(input("Indique o tamanho do  terceiro lado do triângulo:\n"))

if (lado1 == lado2 and lado1 == lado3 and lado2 == lado1 and lado2 == lado3 and lado3 == lado1 and lado3 == lado2):
    print("O triângulo é equilátero.\n")

elif (lado1 != lado2 and lado1 != lado3 and lado2 != lado1 and lado2 != lado3 and lado3 != lado1 and lado3 != lado2):
    print("O triângulo é escaleno.\n")

else: print("O triângulo é isósceles.\n")