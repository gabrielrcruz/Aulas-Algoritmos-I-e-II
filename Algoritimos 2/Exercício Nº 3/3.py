# 3. Ler 2 vetores, R de 5 elementos e S de 10 elementos, ambos de inteiros.
# Gere um vetor X que possua os elementos comuns a R e a S.
# Considere que no mesmo vetor não haverá números repetidos.
#
# Por exemplo:
#
# [Entrada]
# Vetor R = [21, 12, 1, 3, 7]
# Vetor S = [13, 31, 3, 21, 14, 6, 1, 42, 23, 32]
#
# [Saída]
# Vetor X = [21, 1, 3]


listaA = [1,2,3,4,5,6,7,8]
listaB = [1,2,3,4,5,6,7,8,19]
sena = []

for i in range(len(listaA)):
    listaA[i]
    for j in range(len(listaB)):
        if listaA[i] == listaB[j]:
            sena.append(listaA[i])

print(sena)