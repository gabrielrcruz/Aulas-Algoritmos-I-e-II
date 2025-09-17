""""
Escreva um algoritmo, que leia um conjunto de 10 fichas, 
cada uma contendo, a altura e o código do sexo de uma pessoa 
(código = 1 se for masculino e 2 se for feminino), e calcule e imprima: 

- a maior e a menor altura da turma; 
- a média de altura das mulheres; 
- a média de altura da turma. 

"""
altura_turma = []
masculino = []
feminino = []


for i in range(10):
    nome = input("Qual o nome:")
    altura = float(input(f"Qual a Altura de {nome}: "))
    codigo = int(input(f"Digite 1 se {nome} é do sexo Marculino e 2 se {nome} é do sexo Feminino "))
    altura_turma.append(altura)
    if codigo == 1:
        masculino.append(altura)
    if codigo == 2:
        feminino.append(altura)

print(f"a maior altura da turma é {max(altura_turma)} e a menor altura é {min(altura_turma)}")
print(f"a media de altura das mulheres é {(sum(feminino))/len(feminino)}")
print(f"Media de altura da turma é {(sum(altura_turma))/len(altura_turma)}")


