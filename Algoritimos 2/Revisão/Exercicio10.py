#Leia uma palavra e conte quantas vogais
# (a, e, i, o, u) ela possui (use um laço de repetição e condicionais).

contador_vogais = 0
vogais = "aeiou"

palavra = input("Digie uma palavra: ")

for letra in palavra:
    if letra.lower() in vogais:
        contador_vogais += 1

print(contador_vogais)

