# Elabore um algoritmo que leia duas listas de 5 posições, após a leitura 
# realizar a soma e imprima o resultado da soma entre as duas listas de inteiros.



listaA = []
listaB = []

for i in range(9):
    numero = int(input("Digite um numero: "))
    if numero % 2 == 0:
        listaA.append(numero)
    else:
        listaB.append(numero)

print(sum(listaA)+sum(listaB)) 
