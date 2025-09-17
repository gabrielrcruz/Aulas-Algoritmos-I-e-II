#Leia dois números A e B (A < B) e um número K. 
# Calcule a soma de todos os números entre A e B (inclusive) que são divisíveis por K.
#Exemplo: A=10, B=20, K=3 → 12 + 15 + 18 = 45.

NumeroA = int(input("Digite Numero A: "))
NumeroB = int(input("Digite Numero B: "))
NumeroK = int(input("Digite Numero K: "))

inicial = NumeroA
final = NumeroB
lista = []

contador = NumeroA
for i in range(inicial, final):
    
    while contador < final:
        contador = contador + 1
        if contador % NumeroK == 0:
            lista.append(contador)
            
print(lista)
print(sum(lista))
    


        