quant = 0
c = 1
while c <= 5:
    n= float(input(f'Digite o {c} valor: '))
    c = c + 1
    if n > 30:
        quant += 1
    print(n)
print(f' Dos 5 Numeros {quant} sao maiores que 30. ')