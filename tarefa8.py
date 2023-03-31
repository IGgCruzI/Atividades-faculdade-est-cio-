# 8 - Faça um algoritmo que calcule o custo estimado de uma viagem de carro. Posteriormente imprima o resultado.

print("Seja bem vindo ao sistema de cálculo para estimativa de viagens de carro.\n")

distancia = int(input(f"Informe a distância do seu percurso em KM:\n"))
kml = int(input(f"Informe quantos Km seu carro faz por litro de combustível:\n"))

print("Levaremos em conta um valor médio da gasolina sendo R$5,10 o litro.\n")

gasolina1 = 5.10

valor = (distancia/kml)*gasolina1

gasolina = (distancia/kml)

print(f"Sendo assim, você precisará de aproximadamente {gasolina:.2f}L de gasolina.")

print(f"O valor estimado que você gastará é de R${valor:.2f}")

