# 31 -

periodo = input('''
Informe em qual período você estuda, sendo:
M = Matutino;
V = Vespertino;
N = Noturno.
''')

if periodo == 'M' or periodo == "Matutino":
    print("Bom dia!")

elif periodo == "V" or periodo ==  "Vespertino":
    print("Boa tarde!")

elif periodo == "N" or periodo == "Noturno":
    print("Boa noite!")