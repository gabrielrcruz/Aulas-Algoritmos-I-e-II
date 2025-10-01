import random 

matriz = []
for i in range(6):
    numero = []
    for j in range(6):
        #numero.append(random.randrange(0,99))
        valor = int(input("Digite os numeros da matriz: "))
        numero.append(valor)

    matriz.append(numero)

for numeros in matriz:
    print(numeros)
print("_____________________________")
aux = matriz[1]
matriz[1] = matriz[4]
matriz[4] = aux

print("_____________________________")

for numeros in matriz:
    print(numeros)


print("_____________________________")
indice3 = []
indice5 = []

for i in range(6):
    indice3.append(matriz[i][3])

for i in range(6):
    indice5.append(matriz[i][5])

for i in range(5):
    matriz[i][3] = indice5[i]

for i in range(5):
    matriz[i][5] = indice3[i]


for numeros in matriz:
    print(numeros)
print("_____________________________")
print(indice3)
print("_____________________________")
print(indice5)
print("_____________________________")