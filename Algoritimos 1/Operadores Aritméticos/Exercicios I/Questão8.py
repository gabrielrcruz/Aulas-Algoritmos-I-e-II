#Um restaurante a quilo cobra R$45,00 o Kg de refeição. Escreva um algoritmo que leia o 
# peso do prato montado pelo cliente (em quilos) e imprima o valor a pagar. 
# Lembre-se que deve ser informado o peso do prato (tara), para que seja descontado do peso total.

cliente  = float(0.800)
tara = float(0.500)
preco_kg = 45
pagar =  (cliente - tara) * preco_kg
print(round(pagar, 2))