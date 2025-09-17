#Um trabalhador recebeu seu salário e o depositou em sua conta bancária. 
#Esse trabalhador emitiu dois cheques e agora deseja saber seu saldo atual. 
#Sabe-se que cada operação bancária de retirada paga 
#CPMF de 0,38% e o saldo inicial da conta está zerado.

deposito = 1000 
saque1 = 100
saque2 = 100 

taxa1 = saque1 * 0.0037
taxa2 = saque2 * 0.0037

valor_na_conta = deposito - saque1 - saque2 - taxa1 - taxa2

print(valor_na_conta)