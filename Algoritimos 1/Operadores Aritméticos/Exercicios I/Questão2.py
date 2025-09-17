#Faça um programa que receba o valor de um depósito e o valor da taxa de juros anual, 
#calcule e mostre o valor
#do rendimento e o valor total depois do rendimento (após 1 ano);

valor_deposito = float(input("Valor deposito: "))

taxa_anual = float(input("Qual taxa tão pagando"))

valor_rendimento = valor_deposito * taxa_anual / 100

valor_total = valor_rendimento + valor_deposito

print(valor_rendimento)
print(valor_total)





