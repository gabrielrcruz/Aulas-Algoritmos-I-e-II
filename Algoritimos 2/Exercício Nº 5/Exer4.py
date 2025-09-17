matriz = [[1, 2, 3,4,5],[6, 7, 8,9,10],[11, 12, 13,14,15],[16, 17, 18,19,20],[21, 22, 23,24,25]]


print(sum(matriz[4]))


#__________________________________________________________

# 1. Definimos a matriz
matriz = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20],
          [21, 22, 23, 24, 25]]

# 2. Inicializamos uma variável para guardar a soma
soma = 0

# 3. Selecionamos a linha de índice 4
linha_desejada = matriz[4] 

# 4. Percorremos cada elemento da linha selecionada
for numero in linha_desejada:
    # 5. Adicionamos o elemento atual à nossa variável de soma
    soma = soma + numero

# 6. Mostramos o resultado final
print(f"A soma calculada com o laço 'for' é: {soma}")