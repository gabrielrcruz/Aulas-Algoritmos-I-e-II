#Exiba os N primeiros termos da 
#sequência de Fibonacci (ex: 0, 1, 1, 2, 3, 5... para N=5).

sequencia = 5
termo_anterior = 0
termo_atual = 1
for i in range(sequencia):
    print(termo_anterior)
    proximo_termo = termo_anterior + termo_atual
    termo_anterior = termo_atual
    termo_atual = proximo_termo
