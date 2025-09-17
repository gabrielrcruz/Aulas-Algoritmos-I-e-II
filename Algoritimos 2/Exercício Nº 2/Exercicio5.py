# Faça um algoritmo que lê duas listas 
# A e B com 5 elementos cada. Construir uma lista C, 
# sendo este a junção das duas
# outras listas, ou seja, a lista C deverá conter 10 elementos. 
# Mostre no final a lista C.


listaA = []
listaB = []

for i in range(9):
    numero = int(input(f'Digite um numero {1} : '))
    if numero % 2 == 0:
        listaA.append(numero)
    if numero % 2 != 0 and numero != -1:
        listaB.append(numero)
    if numero == -1:
        break

print(listaA+listaB)