#Criar um algoritmo que imprima todos os números de 1 até 10,
#  e a média geral todos eles (intervalo fechado). 

numero = 0 
media = 0

while numero <= 9:
    numero+=1
    media = media + numero / 10
    print(numero)

print(media)
