# 18 -
valorhora = int(input("Qual o valor da sua hora trabalhada?\n"))
horasmes = int(input("Quantas horas você trabalha no mês?\n"))
valormes = valorhora*horasmes

if valormes <= 900:
    IR = 'isento'
    INSS = (valormes*0.1)
    FGTS = (valormes*0.11)
    totaldescontos = (INSS)
    salarioliquido = valormes-totaldescontos
    print(f'''
    Salário Bruto: R${valormes:.2f}
    (-)IR ({IR}): {IR}
    (-)INSS (10%): R${INSS:.2f}
    (-)FGTS (11%): R${FGTS:.2f}
    Total de descontos: R${totaldescontos:.2f}
    Salário Líquido: R${salarioliquido:.2f}\n''')

elif valormes > 900 and valormes <= 1500:
    IR = (valormes*0.05)
    INSS = (valormes*0.1)
    FGTS = (valormes*0.11)
    totaldescontos = (INSS+IR)
    salarioliquido = valormes - totaldescontos
    print(f'''
    Salário Bruto: R${valormes:.2f}
    (-)IR (5%): R${IR:.2f}
    (-)INSS (10%): R${INSS:.2f}
    (-)FGTS (11%): R${FGTS:.2f}
    Total de descontos: R${totaldescontos:.2f}
    Salário Líquido: R${salarioliquido:.2f}\n''')

elif valormes >1500 and valormes <= 2500:
    IR = (valormes*0.1)
    INSS = (valormes * 0.1)
    FGTS = (valormes * 0.11)
    totaldescontos = (INSS + IR)
    salarioliquido = valormes - totaldescontos
    print(f'''
    Salário Bruto: R${valormes:.2f}
    (-)IR (10%): R${IR:.2f}
    (-)INSS (10%): R${INSS:.2f}
    (-)FGTS (11%): R${FGTS:.2f}
    Total de descontos: R${totaldescontos:.2f}
    Salário Líquido: R${salarioliquido:.2f}\n''')

elif valormes > 2500:
    IR = (valormes * 0.2)
    INSS = (valormes * 0.1)
    FGTS = (valormes * 0.11)
    totaldescontos = (INSS + IR)
    salarioliquido = valormes - totaldescontos
    print(f'''
    Salário Bruto: R${valormes:.2f}
    (-)IR ({IR}): {IR:.2f}
    (-)INSS (10%): {INSS:.2f}
    (-)FGTS (11%): {FGTS:.2f}
    Total de descontos: R${totaldescontos:.2f}
    Salário Líquido: R${salarioliquido:.2f}\n''')