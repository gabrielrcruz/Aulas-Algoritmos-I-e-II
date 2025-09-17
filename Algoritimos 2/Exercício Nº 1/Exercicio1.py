#Faça um algoritmo que lê 10 valores para uma variável do tipo 
# vetor de nome x e mostra os 10 valores armazenados na estrutura.


import numpy as np

N = 10 

vetor = np.zeros(N)

for i in range(N):
    vetor[i] = float(input(f'Informe um valor para V[{i}]'))

print(vetor)