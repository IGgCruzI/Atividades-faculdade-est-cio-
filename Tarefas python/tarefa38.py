# 38 -
quilo = 59

pesoprato = 0.2

pesocomida = int(input("Qual foi o peso do seu prato em Kg? Descontaremos o peso do prato que é de 200 gramas.\n"))
valorcomida = (pesocomida - pesoprato) * quilo
print(f'''
O valor a ser pago é de: R${valorcomida}.''')