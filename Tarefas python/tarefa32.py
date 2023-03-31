# 32 -

valor = int(input("Digite o valor que deseja sacar (entre 10 e 600 reais):\n"))

if valor < 10 or valor > 600:
    print("Valor inválido.\n")

else:
    notas100 = valor // 100
    valor = valor % 100
    notas50 = valor // 50
    valor = valor % 50
    notas20 = valor //20
    valor = valor % 20
    notas10 = valor // 10
    valor = valor % 10
    notas5 = valor // 5
    valor = valor % 5
    notas1 = valor
    print(f"Notas de R$100: {notas100}")
    print(f"Notas de R$50: {notas50}")
    print(f"Notas de R$20: {notas20}")
    print(f"Notas de R$10: {notas10}")
    print(f"Notas de R$5: {notas5}")
    print(f"Notas de R$1: {notas1}")