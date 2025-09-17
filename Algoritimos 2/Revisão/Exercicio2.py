# -*- coding: utf-8 -*-
# Acima, uma boa prática para garantir que caracteres como 'ç' e acentos funcionem bem.

# --- Passo 1: Preparação dos Dados (Simulação) ---
# Em vez de pedirmos 100 entradas, vamos criar listas com alguns dados de exemplo.
# A lógica do programa funcionaria exatamente da mesma forma para 100, 1000 ou mais pessoas.

lista_salarios = [1250.00, 1800.50, 980.00, 2500.00, 4200.75, 1490.25, 1500.00, 
                  2100.00, 3150.80, 1100.00, 5600.00, 1320.00, 850.50, 6300.00, 1499.00]

lista_filhos =   [2, 1, 3, 1, 0, 2, 2, 
                  1, 0, 3, 0, 1, 2, 0, 1]

# Obtendo o número total de pessoas na nossa pesquisa (para usar nos cálculos)
total_de_pessoas = len(lista_salarios)

print(f"--- Iniciando análise de dados de {total_de_pessoas} cidadãos. ---\n")


# --- Passo 2: Executando os Cálculos Solicitados ---

# Objetivo A: Calcular a média do salário dessas pessoas
# Para a média, somamos todos os salários e dividimos pelo número de pessoas.
soma_dos_salarios = sum(lista_salarios)
media_salarial = soma_dos_salarios / total_de_pessoas


# Objetivo B: Calcular a média do número de filhos
# A lógica é idêntica à da média salarial.
soma_dos_filhos = sum(lista_filhos)
media_filhos = soma_dos_filhos / total_de_pessoas


# Objetivo C: Encontrar o maior salário
# A função max() é perfeita para isso, ela inspeciona a lista e retorna o maior valor.
maior_salario = max(lista_salarios)


# Objetivo D: Calcular a percentagem de pessoas com salários até R$ 1500,00
# Este é o nosso passo mais elaborado. Precisamos:
# 1. Contar quantas pessoas se encaixam no critério.
# 2. Usar essa contagem para calcular a percentagem.

# 1. Contagem:
# Começamos com um contador zerado.
contador_salarios_ate_1500 = 0
# Usamos um loop 'for' para "visitar" cada salário na nossa lista.
for salario_individual in lista_salarios:
    # Para cada salário visitado, verificamos se ele atende à condição.
    if salario_individual <= 1500:
        # Se sim, incrementamos nosso contador em +1.
        contador_salarios_ate_1500 += 1

# 2. Cálculo da Percentagem:
# A fórmula é: (parte / todo) * 100
percentual = (contador_salarios_ate_1500 / total_de_pessoas) * 100


# --- Passo 3: Apresentação Final dos Resultados ---
# Agora, vamos imprimir tudo de forma clara e organizada, como um relatório.

print("--- Relatório Final da Pesquisa Municipal ---")
print(f"A) Média Salarial da População: R$ {media_salarial:.2f}")
print(f"B) Média de Filhos por Pessoa: {media_filhos:.1f}")
print(f"C) Maior Salário Registrado: R$ {maior_salario:.2f}")
print(f"D) Percentual de Pessoas com Salário até R$ 1500,00: {percentual:.2f}%")
print("\n--- Análise Concluída ---")