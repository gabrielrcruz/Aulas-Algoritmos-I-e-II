matriz = [[1,2,3,4,5],
          [6,7,8,9,10],
          [11,12,13,14,15],
          [16,17,18,19,20],
          [21,22, 23,24,25]]


soma_coluna = 0
# O 'l' representa o índice da linha
for l in range(len(matriz)):
    soma_coluna += matriz[l][1] # Pega o elemento da linha 'l', coluna 1

print(f"A soma da coluna 1 (usando for) é: {soma_coluna}")

print(matriz[4][1]+matriz[3][1]+matriz[2][1]+matriz[1][1]+matriz[0][1])


soma_diagonal = 0
# O 'i' servirá como índice para linha e coluna ao mesmo tempo
for i in range(len(matriz)):
    soma_diagonal += matriz[i][i]

print(f"A soma da diagonal principal (usando for) é: {soma_diagonal}")

print(matriz[0][0]+matriz[1][1]+matriz[2][2]+matriz[3][3]+matriz[4][4])