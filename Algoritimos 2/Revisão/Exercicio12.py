# --- PASSO 1: DIAGNÓSTICO E ENTRADA ---
# Recebemos o valor do usuário e já o convertemos para um número inteiro.
valor_saque = int(input("Digite o valor para saque (múltiplo de 10): "))

# Uma cópia do valor original para usar na mensagem final.
valor_original = valor_saque 

# --- PASSO 1.1: VALIDAÇÃO DA RESTRIÇÃO ---
# Verificamos a restrição mais importante do problema.
# O operador % (módulo) nos dá o RESTO de uma divisão. 
# Se o resto da divisão por 10 não for 0, o número não é múltiplo de 10.
if valor_saque % 10 != 0:
    print("Valor inválido. O caixa opera apenas com múltiplos de R$ 10.")
else:
    # --- PASSO 2: PLANO DE ATAQUE E IMPLEMENTAÇÃO (A LÓGICA CENTRAL) ---
    # Notas disponíveis, da maior para a menor. Isso é crucial.
    notas = [100, 50, 20, 10]
    
    print(f"\nPara sacar R$ {valor_original}, você receberá:")

    # Iteramos sobre cada valor de nota disponível
    for nota in notas:
        # Verifica se o valor a sacar ainda comporta a nota atual
        if valor_saque >= nota:
            # --- O CÁLCULO MÁGICO ---
            # 1. Divisão Inteira (//): Calcula QUANTAS notas de `nota` cabem em `valor_saque`.
            quantidade = valor_saque // nota
            
            # 2. Operador Módulo (%): Calcula o que SOBRA após tirarmos as notas.
            # Este é o novo `valor_saque` para a próxima iteração.
            valor_saque %= nota  # É o mesmo que: valor_saque = valor_saque % nota
            
            # 3. Exibimos o resultado para esta nota específica.
            print(f"- {quantidade} nota(s) de R$ {nota}")

# --- PASSO 5: ANÁLISE (IMPLÍCITA NO CÓDIGO ACIMA) ---
# A lógica garante que, ao final do loop, o valor_saque será 0.