# 26 -

aquis = int(input("Qual foi o valor pago pela aquisição do produto?\n"))

if aquis >= 50:
    valorvenda = (aquis*0.45)+aquis

else:
    valorvenda = (aquis*0.30)+aquis

print(f"O valor da venda será de R$ {valorvenda}.")