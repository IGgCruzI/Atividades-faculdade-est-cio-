# 4 - Faça um algoritmo que leia o nome, a placa do carro, o modelo do carro, e a cor do carro, Posteriormente imprima o resultado de cada variável linha abaixo de linha.
print("\nSeja bem vindo ao sistema de cadastramento de veículos.")
nome =input("Como devemos lhe chamar durante o atendimento?\n")
modelo =input(f"Certo {nome}, qual seria o modelo do seu carro?\n")
placa =input(f"{nome}, agora nos diga a placa do seu {modelo}:\n")
cor =input(f"{nome}, por fim, nos diga a cor do seu carro.\n")
correto = input(f'''Sua informações são:
Nome: {nome};
Modelo: {modelo};
Placa: {placa}:
Cor: {cor}
Digite "sim" para correto e "não" para incorreto.\n''')

while (correto !='sim'):
    print(f"Tudo bem {nome}, vamos recomeçar.\n")
    modelo = input(f"Certo {nome}, qual seria o modelo do seu carro?\n")
    placa = input(f"{nome}, agora nos diga a placa do seu {modelo}\n")
    cor = input(f"{nome}, por fim, nos diga a cor do seu carro.\n")
    correto = input(f'''Sua informações são:
    Nome: {nome};
    Modelo: {modelo};
    Placa: {placa}:
    Cor: {cor}
    Digite "sim" para correto e "não" para incorreto.\n''')