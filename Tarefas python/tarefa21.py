# 21 - Um funcionário recebe um salário fixo mais 4% de comissão sobre vendas. Faça um algoritmo que receba o salário fixo de um funcionário e o valor de suas vendas, calcule e mostre o valor da comissão e o salário final do funcionário.

sfixo = int(input("Digite o valor do seu salário fixo:\n"))
vvendas = int(input("Agora digite o valor de suas vendas:\n"))

comissao = vvendas*0.04
salario = sfixo+comissao

print(f'''
Seu salário fixo é de: R${sfixo}
Sua comissão foi de: R${comissao}
Seu salário final é de: R${salario}''')