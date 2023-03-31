# 15 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escreva: F - Feminino, M – Masculino ou Sexo Inválido.
sexo = input("Defina o seu sexo, sendo 'm' para masculino e 'f' para feminino.\n").upper()

if sexo == "M":
    print("Sexo masculino.\n")

elif sexo == "F":
    print("Sexo feminino.\n")

else: print("Sexo inválido.\n")