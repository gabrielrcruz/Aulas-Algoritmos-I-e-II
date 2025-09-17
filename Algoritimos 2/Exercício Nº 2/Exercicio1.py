#Faça um algoritmo que lê 10 valores para uma variável do tipo
# lista de nome x e mostre os 10 valores armazenados.

numeros = []

for i in range(5):
    # Pede um número ao usuário
    num_digitado = int(input(f"Digite o número {i+1}: "))
    # Adiciona o número na ÚLTIMA posição da lista 'numeros'
    numeros.append(num_digitado)