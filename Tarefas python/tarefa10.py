# 10 - Faça um algoritmo que verifique se o número digitado é menor, maior ou igual a 10 e apresente a mensagem referente ao número.
n = int(input('>>> '))
if n > 10:
    print("É maior que 10")
elif n < 10:
    print("É menor que 10")
else:
    print("É igual a 10")