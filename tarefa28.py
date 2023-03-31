# 28 -

int1 = int(input("Digite um número inteiro:\n"))
int2 = int(input("Digite outro número inteiro:\n"))
real = float(input("Digiten um número real:\n"))

dobro = round((int1*2)*(int2/2))
soma = round((3*int1)*real)
cubo = round(real**3)

print(f'''
O produto do dobro do primeiro com a metade do segundo: {dobro};
A soma do triplo do primeiro com o terceiro: {soma};
O terceiro elevado ao cubo: {cubo}.''')