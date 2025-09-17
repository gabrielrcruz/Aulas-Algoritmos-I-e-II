# Faça um programa que receba o salário base de um funcionário,
# calcule e mostre o salário a receber, sabendo-se que o funcionário tem
# gratificação de 5% sobre o salário base e paga 7% de imposto também sobre o salário base;

salario_base = float(input("Qual seu salário: "))

gratificacao = 0.05 * salario_base
imposto = 0.07 * salario_base


salario_final = salario_base - imposto + gratificacao

print(salario_final)