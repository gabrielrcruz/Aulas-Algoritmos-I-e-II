#Criar um algoritmo que leia dez números inteiros
# e imprima o maior e o menor número.

contador = 1
numero_usuario = int(input(f'Digite o {contador}º numero: '))
menor = numero_usuario
maior = numero_usuario

while contador <= 9:
    numero_usuario = int(input(f'Digite o {contador}º numero: '))
    if numero_usuario < menor:
        menor = numero_usuario
    if numero_usuario > maior:
        maior = numero_usuario 
    contador +=1 
print(maior, menor)
