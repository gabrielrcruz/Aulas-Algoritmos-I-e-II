import random


#Criando a Lista
vetor = []
for i in range(3):
    #numero = random.randrange(-99, 99)
    numero = int(input("Digite os números do vetor: "))
    vetor.append(numero)

print("Numeros do Vetor")
print(vetor)
print("------------------")

#Criando a Matriz
M = []

for i in range(3):
    valor = []
    for l in range(3):
        #n_matriz = random.randrange(0,99)
        n_matriz = int(input("Digite a matriz: "))
        valor.append(n_matriz)
    M.append(valor)

print("Numeros da Matriz")

for numeros in M:
    print(numeros)

print("------------------")

print("Matriz Resultado linha a linha")
resultado = []
for i in range(3):
    tabela = []
    for j in range(3):
        tabela.append(vetor[i]*M[j][i])
    resultado.append(tabela)

for linhas in resultado:
    print(linhas)
