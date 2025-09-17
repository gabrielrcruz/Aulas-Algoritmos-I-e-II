""""Ler 2 duas estruturas (lista, tupla ou conjunto),
 denominada R de 5 elementos e S de 10 elementos, ambos de inteiros. 
 Gere outra estrutura X que possua os elementos comuns a R e a S. 
 Considere que na mesma estrutura não haverá números repetidos."""


R = {1, 2, 3, 4, 5}
S = {1, 2, 3, 4, 5, 6, 7, 8, 19, 10}

# A intersecção usando o operador &
X = R & S

print(X)


# A intersecção usando o método .intersection()
X = R.intersection(S)

print(X)



#usando laços de repetição 

R = set()
S = set()

#for i in range(5):
#    R.add(int(input))
#for i in range(10):
#    S.add(int(input))

x = R & S

print(X)