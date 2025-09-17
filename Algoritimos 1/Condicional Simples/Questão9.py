"""
9) Construa um algoritmo para determinar se o indivíduo está com um peso favorável.
Essa situação é determinada através do IMC (Índice de Massa Corpórea), que é definida
como sendo a relação entre o peso (PESO) e o quadrado da Altura (ALTURA) do indivídu-o.
Ou seja,

      PESO
IMC = -------
    ALTURA**2

e, a situação do peso é determinada pela tabela abaixo:

Condição           Situação
------------------ ----------------
IMC abaixo de 20   Abaixo do peso
IMC de 20 até 25   Peso Normal
IMC de 25 até 30   Sobre Peso
IMC de 30 até 40   Obeso
IMC de 40 e acima  Obeso Mórbido
"""

# --- Dados de Entrada ---
peso = 132.20
altura = 1.82

# --- Cálculo do IMC ---
# A fórmula é o peso dividido pelo quadrado da altura.
calculo_imc = peso / (altura ** 2)

# --- Impressão do resultado numérico do IMC (opcional) ---
# Usamos uma f-string para formatar o número para duas casas decimais.
print(f"Seu IMC é: {calculo_imc:.2f}")

# --- Estrutura de Decisão (if/elif/else) ---
# Com base na tabela, o programa verifica em qual faixa o IMC se encaixa.

situacao = "" # Variável para armazenar a situação

if calculo_imc < 20:
    situacao = "Abaixo do peso"
elif calculo_imc < 25: # Não precisa verificar se é >= 20, pois o if anterior já cobriu isso
    situacao = "Peso Normal"
elif calculo_imc < 30:
    situacao = "Sobre Peso"
elif calculo_imc < 40:
    situacao = "Obeso"
else: # Se não for nenhuma das anteriores, significa que é 40 ou mais
    situacao = "Obeso Mórbido"

# --- Impressão do Resultado Final ---
print(f"Situação: {situacao}")