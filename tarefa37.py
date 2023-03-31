# 37 - 
paozinho = 1
broa = 3.50

quantidadepaozinho = int(input("Quantos pães foram vendidos hoje?\n"))
quantidadebroa = int(input("E quantas broas foram vendidas hoje?\n"))

valorpaozinho = quantidadepaozinho * paozinho
valorbroa = quantidadebroa * broa

valortotal = valorpaozinho + valorbroa

poupança = valortotal * 0.10

print(f'''
Valor total Pães: R${valorpaozinho};
Valor total Broas: R${valorbroa};
Valor total: R${valortotal};
Valor para Poupança: R${poupança}.''')