#Faça um algoritmo que lê 10
#valores para uma variável do tipo vetor e mostre qual a posição está
# armazenado o maior e o menor valor no vetor.

# Primeiro, precisamos importar a biblioteca. A convenção é usar o apelido 'np'.
import numpy as np

# Vamos criar um array NumPy. A sintaxe é parecida com a de uma lista.
vetor_np = np.array([25, 10, 42, 15, 50, 9, 33])

print(f"Nosso array NumPy: {vetor_np}")

# --- A MÁGICA DO NUMPY ---
# Encontrar a POSIÇÃO do maior valor com uma única função.
posicao_do_maior = np.argmax(vetor_np)
posicao_do_menor = np.argmin(vetor_np)
# E se você quiser o valor também, pode usar np.max() ou acessar pela posição.
maior_valor = vetor_np[posicao_do_maior] # ou pode usar maior_valor = np.max(vetor_np)
menor_valor = vetor_np[posicao_do_menor]

print("\n--- Resultados com NumPy ---")
print(f"O maior valor é {maior_valor}.")
print(f"Sua posição (índice) é: {posicao_do_maior}")
print(f"O maior valor é {menor_valor}.")
print(f"Sua posição (índice) é: {posicao_do_menor}")
