#Escreva um algoritmo que receba 15 números e imprima quantos
#  números maiores que 30 foram digitados. 

maior_que_30 = 0

for i in range(15):
    numero = int(input("Digite Numero: "))
    if numero >= 30:
        maior_que_30 += 1
print(maior_que_30)