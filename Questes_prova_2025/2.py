import random

lista = []

for i in range(25):
    valor = int(input("Digite valor: "))
    lista.append(valor)
    
print(lista)
print(len(lista))

lista = lista[::-1]

for numero in range(25):
    if lista[numero] < 0:
        lista[numero] = (lista[numero] - lista[numero]) - lista[numero]
    else: 
        lista[numero] = (lista[numero] - lista[numero]) - lista[numero]

print(lista)
print(len(lista))