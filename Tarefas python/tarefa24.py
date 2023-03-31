#24 -
queijo = 2*50
presunto = 50
hamburguer = 100

pesosanduiche = queijo+presunto+hamburguer

qntsanduiche = int(input("Informe a quantidade de sanduiches:\n"))

qntqueijo = (qntsanduiche*queijo)/1000
qntpresunto = (qntsanduiche*presunto)/1000
qnthamburguer = (qntsanduiche*hamburguer)/1000

print(f'''
Quantidade de queijo: {qntqueijo}Kg
Quantidade de presunto: {qntpresunto}Kg
Quantidade de Hamburguer: {qnthamburguer}Kg''')