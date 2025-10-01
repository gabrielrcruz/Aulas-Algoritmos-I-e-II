valor = []

positivos = []
negativos = []

for i in range(8):
    numero = int(input("Digite: "))
    valor.append(numero)
    if valor[i] < 0:
        negativos.append(valor[i])
    if valor[i] > 0:
        positivos.append(valor[i])


print(valor)
print(positivos)
print(negativos)

