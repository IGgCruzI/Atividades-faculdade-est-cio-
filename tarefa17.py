# 17 -


salario = int(input("Informe seu salário para saber o seu ajuste:\n"))

if salario >= 0 and salario <= 280:
    porcentagemaumento = 0.20
    ajuste = (salario*porcentagemaumento)+salario
    aumento = (salario*porcentagemaumento)
    percentual = '20%'

elif salario > 280 and salario <= 700:
    porcentagemaumento = 0.15
    ajuste = (salario*porcentagemaumento)+salario
    aumento = (salario*porcentagemaumento)
    percentual = '15%'

elif salario > 700 and salario <= 1500:
    porcentagemaumento = 0.1
    ajuste = (salario*porcentagemaumento)+salario
    aumento = (salario*porcentagemaumento)
    percentual = '10%'

elif salario > 1500:
    porcentagemaumento = 0.05
    ajuste = (salario*porcentagemaumento)+salario
    aumento = (salario*porcentagemaumento)
    percentual = '5%'


print(f'''
Salário antes do ajuste: R${salario} ;
Percentual de aumento aplicado: {percentual}
Valor do aumento: R${aumento}
Novo salário: R${ajuste}
''')