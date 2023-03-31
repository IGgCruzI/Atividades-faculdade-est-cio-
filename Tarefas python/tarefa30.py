# 30 -

pesopeixe = int(input("Digite o peso do peixe em Kg:\n"))
excesso = (pesopeixe-50)
pesoexcedente = (50-excesso)

if excesso <= 0:
    multa = "Sem multa aplicada.\n"

else: multa = (excesso*4)


print(f'''
Peso do peixe: {pesopeixe}Kg;
Excesso: {excesso}Kg;
Peso excedente: {pesoexcedente}Kg;
Valor da Multa: R${multa}.''')