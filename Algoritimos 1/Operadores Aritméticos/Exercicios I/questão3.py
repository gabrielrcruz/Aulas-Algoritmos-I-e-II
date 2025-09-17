#Sabe-se que:
#1 Pé =12 polegadas
#1 jarda = 3 pés
#1 milha = 1.760 jardas
#Faça um programa que receba uma medida em pés, faça as conversões e a seguir mostre os resultados em:
#Polegadas
#Jardas
#Milhas

valor_pe = float(input("Digite o valor em pe"))


polegada = valor_pe * 12 / 1
jarda = valor_pe * 1 / 3
milha = valor_pe * 1 / 5280

print(polegada, jarda, milha)



