import random

lista = []

par = []

impar = []

for i in range(100):
    #lista.append(random.randrange(0,99))
    lista = int(input("Digire os números da lista"))
    if lista[i] % 2 == 0:
        par.append(lista[i])
    if lista[i] % 2 != 0:
        impar.append(lista[i])
print(lista)
print(len(par))
print(sum(impar)/len(impar))