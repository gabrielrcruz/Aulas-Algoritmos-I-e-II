#Altere o algoritmo anterior para que ele realize o 
#produto da primeira lista, pelo inverso da segunda lista.

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
        

#print(sum(listaA)+sum(listaB)) 
#print((len(listaA) + listaB[::-1]))
soma = sum(listaB[::-1]) + len(listaA)
print(soma)
#print(listaB[::-1])
#print(len(listaA))