# 22 - Faça um algoritmo que receba o preço de um produto, calcule e mostre o novo preço, sabendo-se que este sofreu um desconto de 10%.

precoa = int(input("Digite o valor do produto:\n"))

precon = precoa-(precoa*0.1)

print(f"O novo preço é de R${precon}.")