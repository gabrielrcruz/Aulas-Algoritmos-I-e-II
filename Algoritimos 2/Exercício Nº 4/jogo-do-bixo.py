""""Ler uma estrutura (lista, tupla ou conjunto), R de 5 elementos, inteiros, contendo o resultado da LOTO. A seguir ler outra estrutura (lista, tupla ou conjunto), 
A de 10 elementos inteiros contendo uma aposta. A seguir imprima quantos pontos fez o apostador."""

resultado = {23,27,32,54,56,59}

jogo = {2,27,3,54,56,5}

#essa bruxaria aqui compara o resultado com o jogo esse elemento aqui - &
# e o len verifica o tamanho do conjunto
print (len(resultado & jogo))

