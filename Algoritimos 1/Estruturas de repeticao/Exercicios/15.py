"""""Deseja-se estudar o perfil dos consumidores de energia elétrica de uma cidade, 
para um dado mês do ano. Para tanto, deverão ser lidos os seguintes dados para cada um dos 
n consumidores de uma amostragem (n deve ser solicitado ao usuário no início do programa): 

consumo do mês, em kWh; 
código do tipo de consumidor (1 para residencial, 2 para comercial e 3 para industrial); 
Antes de ler os dados dos consumidores, o preço do kWh deve ser fornecido ao programa. 

Escrever um programa que leia os dados indicados acima e calcule e imprima: 

- Para cada consumidor, o total a pagar; 
- O maior consumo verificado na amostra de consumidores; 
- O menor consumo verificado na amostra de consumidores; 
- O total do consumo para cada um dos três tipos de consumidores; 
"""""

# --- Fase 1: Setup e Entradas Iniciais ---
# Estas são as informações que valem para toda a "operação", como regras de negócio.
# Pedimos uma única vez, antes do trabalho principal começar.
print("--- Sistema de Análise de Consumo de Energia ---")
preco_kwh = float(input("Forneça o preço do kWh (ex: 0.75): "))
n_consumidores = int(input("Quantos consumidores serão analisados na amostragem? "))

# --- Fase 2: Inicialização das Variáveis de Análise Agregada ---
# Sem listas, estas variáveis são nossa única memória.
# Elas guardarão o estado da análise ao longo do tempo.

# Para encontrar o maior e menor, precisamos de um ponto de partida.
# Uma técnica comum é usar o primeiro consumidor como referência inicial.
# Uma variável "flag" controla isso.
primeiro_consumidor = True
maior_consumo = 0
menor_consumo = 0

# Acumuladores para o consumo total de cada categoria.
total_consumo_residencial = 0
total_consumo_comercial = 0
total_consumo_industrial = 0


# --- Fase 3: Loop Principal - Processamento em Tempo Real ---
# O coração da operação. Iteramos pelo número de consumidores informado.
# Cada consumidor é processado e "esquecido". Apenas as variáveis agregadas são atualizadas.

if n_consumidores > 0:
    for i in range(n_consumidores):
        print(f"\n--- Dados do Consumidor {i + 1}/{n_consumidores} ---")
        
        consumo_mes = float(input("Consumo do mês (kWh): "))
        
        # Validação da entrada do tipo de consumidor
        codigo_tipo = 0
        while codigo_tipo not in [1, 2, 3]:
            codigo_tipo_input = input("Código do consumidor (1-Residencial, 2-Comercial, 3-Industrial): ")
            if codigo_tipo_input.isdigit():
                codigo_tipo = int(codigo_tipo_input)
            if codigo_tipo not in [1, 2, 3]:
                print("Código inválido. Por favor, digite 1, 2 ou 3.")

        # a) Para cada consumidor, o total a pagar (Cálculo Imediato)
        # Esta informação é calculada e exibida na hora. Não precisamos guardá-la.
        total_a_pagar = consumo_mes * preco_kwh
        print(f"-> Total a pagar por este consumidor: R$ {total_a_pagar:.2f}")

        # b) e c) O maior e menor consumo verificado
        if primeiro_consumidor:
            # No primeiro loop, o maior e o menor consumo são o consumo atual.
            maior_consumo = consumo_mes
            menor_consumo = consumo_mes
            primeiro_consumidor = False # Desarmamos a flag.
        else:
            # Para os demais, comparamos com os valores que já temos guardados.
            if consumo_mes > maior_consumo:
                maior_consumo = consumo_mes
            if consumo_mes < menor_consumo:
                menor_consumo = consumo_mes
        
        # d) O total do consumo para cada um dos três tipos
        # Usamos uma estrutura de decisão para direcionar o valor do consumo
        # para o "balde" (acumulador) correto.
        if codigo_tipo == 1:
            total_consumo_residencial += consumo_mes
        elif codigo_tipo == 2:
            total_consumo_comercial += consumo_mes
        elif codigo_tipo == 3:
            total_consumo_industrial += consumo_mes

# --- Fase 4: Relatório Final ---
# Após o loop terminar, apresentamos o resumo da operação
# com base no estado final das nossas variáveis de análise.
print("\n\n--- Relatório Final da Amostragem ---")
if n_consumidores > 0:
    print(f"Maior consumo verificado na amostra: {maior_consumo:.2f} kWh")
    print(f"Menor consumo verificado na amostra: {menor_consumo:.2f} kWh")
    print("\nTotal de consumo por categoria:")
    print(f"  - Residencial (1): {total_consumo_residencial:.2f} kWh")
    print(f"  - Comercial   (2): {total_consumo_comercial:.2f} kWh")
    print(f"  - Industrial  (3): {total_consumo_industrial:.2f} kWh")
else:
    print("Nenhum consumidor foi analisado.")