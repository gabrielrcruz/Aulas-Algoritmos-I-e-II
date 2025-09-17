
#Faça um algoritmo que lê 5 
#valores para uma variável do tipo vetor e determine
#  a média de todos os valores armazenados no vetor.


import numpy as np

N = 5 

vetor = np.zeros(N)

for i in range(N):
    vetor[i] = float(input(f'Informe um valor para V[{i}]'))

print((vetor[0] + vetor[1] + vetor[2] + vetor[3] + vetor[4]) / N)
print(vetor)