#Peça um número inteiro positivo N e calcule a soma de todos os números de 1 até N.
#Exemplo: Se N = 5 → 1 + 2 + 3 + 4 + 5 = 15.


numero = int(input("Digite um numero: "))
soma = 0
inicial = 0
for i in range(numero):
    inicial+=1
    soma = soma + inicial
    print(soma)

print(soma)