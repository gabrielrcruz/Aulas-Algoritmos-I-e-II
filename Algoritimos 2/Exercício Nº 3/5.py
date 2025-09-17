""""Faça um programa que preencha dois vetores
de dez elementos numéricos cada um e mostre o vetor
resultante da intercalação deles:"""

listaA = [1,2,3,4,5,6,7,8,9,10]
listaB = [11,12,13,14,15,16,17,18,19,10]

lista_intercalada_loop = []

for item1, item2 in zip(listaA,listaB):
    lista_intercalada_loop.append(item1)
    lista_intercalada_loop.append(item2)
    