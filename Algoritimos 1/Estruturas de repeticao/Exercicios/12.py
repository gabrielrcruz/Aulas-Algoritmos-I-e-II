#Escreva um algoritmo que leia 20
#números e imprima a soma dos positivos e o total de números negativos. 

numeros_negativos = 0
numeros_positivos = 0

for i in range(20):
    numeros = int(input("Digite um número: "))
    if numeros >= 0:
        numeros_positivos = numeros_positivos + numeros
    if numeros < 0:
        numeros_negativos+=1

print(numeros_positivos, numeros_negativos)