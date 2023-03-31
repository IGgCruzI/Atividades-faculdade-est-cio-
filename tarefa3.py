# 3 - Faça um algoritmo que leia o nome, o título eleitoral e o número do candidato. Posteriormente imprima o resultado de cada variável linha abaixo de linha.
print("Seja bem vindo a área do Eleitor Digital.\n")

nome = input("Para prosseguirmos, nos informe seu nome:\n")

print(f"Bem vindo {nome}!")

titulo = int(input("Nos informe qual seu título eleitoral, para confirmarmos seu acesso:\n"))

print(f"{nome}, agora você está logado!\n")

candidato = int(input(f"{nome}, agora digite o número do candidato de sua escolha. Lembrando, o voto é secreto, não divulgue seu voto!\n"))

correto = input(f'''Certo, {nome}, vamos conferir suas informações:

Nome: {nome};
Título eleitoral: {titulo};
Número do Candidato: {candidato}.
As informações assim estão corretas?

Caso estejam corretas, digite "sim", caso estejam erradas digite "não":
\n''')

while (correto != 'sim'):
    print("Tudo bem, nesse caso, vamos recomeçar")
    print("Seja bem vindo a área do Eleitor Digital.\n")

    nome = input("Para prosseguirmos, nos informe seu nome:\n")

    print(f"Bem vindo {nome}!")

    titulo = int(input("Nos informe qual seu título eleitoral, para confirmarmos seu acesso:\n"))

    print(f"{nome}, agora você está logado!\n")

    candidato = int(input(f"{nome}, agora digite o número do candidato de sua escolha. Lembrando, o voto é secreto, não divulgue seu voto!\n"))

    correto= input(f'''Certo, {nome}, vamos conferir suas informações:

Nome: {nome};
Título eleitoral: {titulo};
Número do Candidato: {candidato}.
As informações assim estão corretas?

Caso estejam corretas, digite "sim", caso estejam erradas digite "não":
''')