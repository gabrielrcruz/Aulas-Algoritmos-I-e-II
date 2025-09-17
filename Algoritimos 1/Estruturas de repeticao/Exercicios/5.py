#Escreva um algoritmo que receba cinco números do usuário e imprima o cubo de cada número. 

numero = 0
while numero <= 9:
    numero+=1
    numero_digitado = int(input(f'Digite {numero}º '))
    print(f'o cubo de  {numero_digitado} é {numero_digitado ** 3}')
    

