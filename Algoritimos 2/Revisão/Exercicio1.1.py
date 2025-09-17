#Faça um programa que solicite valores inteiros fornecidos pelo usuário até ele informar o 
##valor 0 (zero). Em seguida, identifique e exiba quantos 
#números ímpares e os pares foram fornecidos, sem considerar o valor 0.

numero_par = 0
numero_impar = 0

while True:
    numero = int(input("Digite Um numero ou digite 0 para sair: "))
    if numero % 2 == 0:
        numero_par+=1
        if numero == 0:
            numero_par-=1
    if numero % 2 != 0:
        numero_impar+=1
    if numero == 0:
        break
print(f'Aqui temos uma sequencia de {numero_par} numeros pares e {numero_impar} numeros impares')
