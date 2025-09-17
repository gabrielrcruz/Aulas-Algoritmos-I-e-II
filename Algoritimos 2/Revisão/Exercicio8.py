#Verifique se um número N é perfeito (igual à soma de seus divisores próprios, exceto ele mesmo).
#Exemplo: 6 (1 + 2 + 3 = 6) → É perfeito.

numero = int(input("Digite um Número para saber se é perfeito: "))

lista = []

contador = 0

while contador < numero:
    contador = contador + 1
    if numero % contador != 0 or contador == numero:
        continue
    else:
        lista.append(contador)
if sum(lista) == numero:
    print(lista)
else:
    print("numero errado.")