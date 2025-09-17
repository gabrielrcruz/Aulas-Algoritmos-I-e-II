# --- 1. Preparação das Variáveis ---
# Inicializamos os contadores para saber a quantidade de números.
contador_pares = 0
contador_impares = 0

# Criamos as listas vazias que vão armazenar os números.
# Pense nelas como caixas que começam vazias e vamos enchendo.
numeros_pares = []
numeros_impares = []

print("Digite quantos valores inteiros quiser. Para terminar, digite 0.")

# --- 2. Loop para Coletar e Organizar os Dados ---
while True:
    # Pedimos ao usuário para digitar um número.
    numero_digitado = int(input("Digite um valor (ou 0 para sair): "))

    # Se o número for 0, o loop é interrompido com o 'break'.
    if numero_digitado == 0:
        break # Encerra o loop.

    # Verificamos se o número é par.
    # O operador '%' (módulo) nos dá o resto de uma divisão.
    # Se o resto da divisão por 2 for 0, o número é par.
    elif numero_digitado % 2 == 0:
        print(f"O número '{numero_digitado}' é par.")
        contador_pares += 1 # Incrementamos o contador de pares.
        numeros_pares.append(numero_digitado) # Adicionamos o número à lista de pares.

    # Se não for 0 e não for par, só pode ser ímpar.
    else:
        print(f"O número '{numero_digitado}' é ímpar.")
        contador_impares += 1 # Incrementamos o contador de ímpares.
        numeros_impares.append(numero_digitado) # Adicionamos o número à lista de ímpares.

# --- 3. Apresentação dos Resultados ---
print("\n--- Análise Finalizada! ---")

# Mostramos a quantidade de números pares e a lista deles.
print(f"\nTotal de números pares digitados: {contador_pares}")
print(f"Os números pares foram: {numeros_pares}")

# Mostramos a quantidade de números ímpares e a lista deles.
print(f"\nTotal de números ímpares digitados: {contador_impares}")
print(f"Os números ímpares foram: {numeros_impares}")