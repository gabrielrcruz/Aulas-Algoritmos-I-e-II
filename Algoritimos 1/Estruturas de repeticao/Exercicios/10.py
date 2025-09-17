#Criar um algoritmo que leia os limites inferior e superior de um intervalo
#e imprima todos os números pares no intervalo aberto e seu somatório. 
soma = 0

for i in range(1,10):
    i = int(input("Digite Um numero: "))
    if i % 2 == 0:
        print(i)
        soma = soma + i
        
print(soma)

