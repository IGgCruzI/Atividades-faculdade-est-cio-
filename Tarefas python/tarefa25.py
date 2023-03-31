# 25 -

pequena = 10
media = 12
grande = 15

qntpequenas = int(input("Qual a quantidade de camisetas pequenas você deseja?\n"))
qntmedias = int(input("Qual a quantidade de camisetas médias você deseja?\n"))
qntgrandes = int(input("Qual a quantidade de camisetas grandes você deseja?\n"))

valortotal = (qntpequenas*10)+(qntmedias*12)+(qntgrandes*15)

print(f"O valor total da sua compra é de R${valortotal}.")