#Faça um programa que leia o nome do usuário e o imprima na vertical, em forma de escada, usando apenas letras maiúsculas. 
#Exemplo: Nome = RAFAEL
#Resultado gerado pelo programa: 
#R
#RA
#RAF
#RAFA
#RAFAE
#RAFAEL



vogais = ("a", "e", "i", "o", "u")

palavra = input("Digite uma palavra: ")

vogais_na_palavra = []
for vogais in palavra:
    vogais_na_palavra.append(vogais)
    print(vogais_na_palavra)