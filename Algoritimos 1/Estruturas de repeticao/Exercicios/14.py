"""
Um cinema possui capacidade de 20 lugares e está sempre com ocupação total. 
Certo dia, cada espectador respondeu a um questionário, em que constava: 
- sua idade; 
- sua opinião em relação ao filme, segundo as seguintes notas: 

Nota | Significado
-----|------------
  A  | Ótimo
  B  | Bom
  C  | Regular
  D  | Ruim
  E  | Péssimo

Elabore um algoritmo que, lendo estes dados, calcule e imprima: 
a) a quantidade de respostas ótimo; 
b) a diferença percentual entre respostas bom e regular; 
c) a média de idade das pessoas que responderam ruim; 
d) a percentagem de respostas péssimo e a maior idade que utilizou esta opção; 
e) a diferença de idade entre a maior idade que respondeu ótimo e a maior idade que respondeu ruim. 
"""

# --- Fase 1: Inicialização das Variáveis de Análise ---
# Sem listas, precisamos de uma variável para cada pedaço de informação
# que queremos rastrear ao longo do tempo. Elas são nossos "post-its".
total_espectadores = 20

# a) Quantidade de respostas "ótimo"
qtd_otimo = 0

# b) Contadores para "bom" e "regular"
qtd_bom = 0
qtd_regular = 0

# c) Variáveis para calcular a média de idade de quem respondeu "ruim"
qtd_ruim = 0
soma_idade_ruim = 0

# d) Variáveis para a percentagem e maior idade de quem respondeu "péssimo"
qtd_pessimo = 0
maior_idade_pessimo = 0

# e) Variáveis para encontrar as maiores idades para "ótimo" e "ruim"
maior_idade_otimo = 0
maior_idade_ruim = 0


# --- Fase 2: Coleta e Processamento em Tempo Real ---
# O loop único. Cada espectador é uma oportunidade única de atualizar
# nossas variáveis. O que não for capturado aqui, se perde para sempre.
print("--- Questionário do Cinema (Modo de Processamento Contínuo) ---")
for i in range(total_espectadores):
    print(f"\n--- Espectador {i + 1}/{total_espectadores} ---")
    idade = int(input("Qual sua idade: "))
    
    nota = 0
    while nota not in [1, 2, 3, 4, 5]:
        nota_input = input("Digite sua nota para o Filme:\n 1 - Ótimo\n 2 - Bom\n 3 - Regular\n 4 - Ruim\n 5 - Péssimo\nSua nota: ")
        if nota_input.isdigit():
            nota = int(nota_input)
        if nota not in [1, 2, 3, 4, 5]:
            print("Opção inválida. Por favor, digite um número de 1 a 5.")

    # A central de decisões. Para cada nota, atualizamos o estado do nosso sistema.
    if nota == 1:  # Ótimo
        qtd_otimo += 1
        # É a maior idade que vimos ATÉ AGORA para esta categoria?
        if idade > maior_idade_otimo:
            maior_idade_otimo = idade
            
    elif nota == 2:  # Bom
        qtd_bom += 1
        
    elif nota == 3:  # Regular
        qtd_regular += 1
        
    elif nota == 4:  # Ruim
        qtd_ruim += 1
        soma_idade_ruim += idade # Acumulamos a idade para a média futura
        if idade > maior_idade_ruim:
            maior_idade_ruim = idade
            
    elif nota == 5:  # Péssimo
        qtd_pessimo += 1
        if idade > maior_idade_pessimo:
            maior_idade_pessimo = idade

# --- Fase 3: Cálculos Finais e Apresentação ---
# O loop terminou. Nenhuma informação nova chegará.
# Usamos o estado final das nossas variáveis para gerar o relatório.

# b) Diferença percentual entre bom e regular
diff_percentual_bom_regular = abs(qtd_bom - qtd_regular) / total_espectadores * 100

# c) Média de idade de quem respondeu "ruim"
if qtd_ruim > 0:
    media_idade_ruim = soma_idade_ruim / qtd_ruim
else:
    media_idade_ruim = 0

# d) Percentagem de respostas "péssimo"
percentual_pessimo = (qtd_pessimo / total_espectadores) * 100

# e) Diferença de idade
# Se uma das categorias não teve votos, a "maior idade" ainda será 0.
# A função abs() garante que a diferença seja sempre um valor positivo.
diff_idade_otimo_ruim = abs(maior_idade_otimo - maior_idade_ruim)

# --- Apresentação dos Resultados ---
print("\n\n--- Resultados da Pesquisa ---")
print(f"a) Quantidade de respostas 'Ótimo': {qtd_otimo}")
print(f"b) Diferença percentual entre 'Bom' e 'Regular': {diff_percentual_bom_regular:.2f}%")
if media_idade_ruim > 0:
    print(f"c) Média de idade das pessoas que responderam 'Ruim': {media_idade_ruim:.1f} anos")
else:
    print("c) Média de idade das pessoas que responderam 'Ruim': Ninguém respondeu 'Ruim'.")
print(f"d) Percentagem de respostas 'Péssimo': {percentual_pessimo:.2f}%")
if qtd_pessimo > 0:
    print(f"   Maior idade que respondeu 'Péssimo': {maior_idade_pessimo} anos")
else:
    print("   Maior idade que respondeu 'Péssimo': Ninguém respondeu 'Péssimo'.")
if qtd_otimo > 0 and qtd_ruim > 0:
    print(f"e) Diferença de idade entre o mais velho que respondeu 'Ótimo' e o mais velho que respondeu 'Ruim': {diff_idade_otimo_ruim} anos")
else:
    print("e) Não foi possível calcular a diferença de idade pois não houve respostas em 'Ótimo' e/ou 'Ruim'.")