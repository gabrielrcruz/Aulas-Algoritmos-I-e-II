"""Faça um algoritmo que lê 5 valores para uma variável 
do tipo vetor e determine o maior e o menor valor armazenado no vetor."""


import numpy as np

N = 5 

vetor = np.zeros(N)

menor = 0
maior = 0

for i in range(N):
    
    vetor[i] = float(input(f'Informe um valor para V[{i}]'))
    if i > maior:
        maior = i
    if i < menor:
        menor = i

print(menor)
print(maior)