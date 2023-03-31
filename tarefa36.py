# 36 - 
codigo100 = 11.20
codigo101 = 8.30
codigo102 = 11.50
codigo103 = 16.20
codigo201 = 6.00
codigo202 = 7.50
codigo203 = 4.70

lanche = int(input('''Digite o código referente ao lanche que deseja, de acordo com a tabela de códigos abaixo:
Cachorro Quente - 100: R$ 11,20
Ovo Simples     - 101: R$ 8,30
Bauru com Ovo   - 102: R$ 11,50
Hambúrguer      - 103: R$ 16,20
'''))
if lanche == 100:
    valorl = 11.20
    
elif lanche == 101:
    valorl = 8.30

elif lanche == 102:
    valorl = 11.50

elif lanche == 103:
    valorl = 16.20


bebida = int(input('''Digite o código referente a bebida que deseja, de acordo com a tabela de códigos abaixo:
Refrigerante    - 201: R$ 6,00
Suco            - 202: R$ 7,50
Água Mineral    - 203: R$ 4,70
'''))
if bebida == 201:
    valorb = 6.00

elif bebida == 202:
    valorb = 7.50

elif bebida == 203:
    valorb = 4.70

    valortotal = valorl + valorb
valortotal = valorl + valorb

print(f'''Valor total: R${valortotal:.2f}
    ''')