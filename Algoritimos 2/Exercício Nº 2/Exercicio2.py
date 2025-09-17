# Faça um algoritmo que lê 10 valores para uma variável do tipo lista
# de nome x. Após completar toda a leitura da lista, verificar se cada valor
# armazenado na lista é par ou ímpar. Se for par, fazer com que o valor seja 
# atualizado para o resultado da multiplicação do valor contido pelo índice. 
# Se for impar, fazer com que a lista receba o valor do seu próprio índice.

numeros = []

for i in range(5):
    # Pede um número ao usuário
    num_digitado = int(input(f"Digite o número {i+1}: "))
    # Adiciona o número na ÚLTIMA posição da lista 'numeros'
    numeros.append(num_digitado)
    print(numeros)
    

#if numeros[0] % 2 != 0:
#    numeros[0] = numeros.index[0]

numero1 = numeros[0]
numero2 = numeros[2]
print(numeros.index(numero2))