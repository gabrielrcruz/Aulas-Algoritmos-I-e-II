""""Ler um vetor R de 5 elementos, inteiros, contendo o resultado da LOTO. 
A seguir ler um vetor A de 10 elementos inteiros contendo uma aposta. 
A seguir imprima quantos pontos fez o apostador."""


resultado = [21,31,41,53,58]

aposta = [21,31,41,53,58,60,22,23,24,50]

pontos = 0

for i in range(len(resultado)):
#    print(resultado[i])
    if resultado[i] in aposta:
        pontos+=1
#    for j in range(len(aposta)):
#        if resultado[i] == aposta[j]:
#            pontos=+ 1

print(pontos)
