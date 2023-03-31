# 14 - Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após, calcule e escreva o saldo atual (saldo atual = saldo - débito + crédito). Também teste se saldo atual for maior ou igual a zero. Em seguida escreva a mensagem 'Saldo Positivo', senão, escrever a mensagem 'Saldo Negativo'.

nome = input("Seja bem vindo ao Banco Estácio, qual o seu nome?\n")
numeroconta = int(input(f"{nome}, qual o número da sua conta bancária para que possamos verificar suas informações.\n"))
saldo = int(input(f"{nome}, conta acessada. Nos informe o seu saldo:\n"))
debito = int(input(f"{nome}, qual o valor do seu débito?\n"))
credito = int(input(f"Por fim, qual o valor do seu crédito?\n"))

saldoatual = (saldo-debito)+credito

if saldoatual >= 0:
    print(f"Seu saldo da conta é de {saldoatual} e o valor é positivo.\n")

else: print(f"Seu saldo da conta é de R${saldoatual} e o valor é negativo.\n")

