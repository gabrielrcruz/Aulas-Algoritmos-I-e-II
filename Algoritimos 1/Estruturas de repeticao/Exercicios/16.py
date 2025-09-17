

N = int(input("Digite o numero de alunos:"))

aprovados = 0
reprovados = 0
contador = N
for i in range(N):
    contador -= 1
    while True:
        av1 = float(input("Nota Avaliação 1: "))
        av2 = float(input("Nota Avaliação 2: "))
        t1 = float(input("Nota Trabalho 1: "))
        t2 = float(input("Nota Trabalho 2: "))
        t3 = float(input("Nota Trabalho 3: "))
        t4 = float(input("Nota Trabalho 4: "))
        if (0.3 * av1) + (0.3 * av2) + (0.4 * (t1 + t2 + t3 + t4 / 4)) >= 7:
            print("Aprovado")
            aprovados =+ 1
        else:
            print("Reprovado")
            reprovados =+ 1
        if contador == 0:
            break
print(aprovados,reprovados)