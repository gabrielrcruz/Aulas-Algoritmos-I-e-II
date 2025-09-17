#Escreva um algoritmo que leia dez números do usuário e imprima a metade de cada número. 
numero = 0
while numero <= 9:
    numero+=1
    numero_digitado = int(input(f'Digite {numero}º '))
    print(f'a metade de {numero_digitado} é {numero_digitado/2}')
    
