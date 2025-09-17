#Uma padaria vende uma certa quantidade de pães franceses e uma quantidade
#de broas a cada dia. Cada pão custa R$ 0,50 e a broa custa R$ 1,50. Ao final do dia, 
#o dono quer saber quanto arrecadou com a venda dos pães e broas (juntos), e quanto deve 
# guardar numa conta de poupança (10% do total arrecadado). Faça um algoritmo para ler
#as quantidades de pães e de broas, e depois calcular os dados solicitados.

quantidade_pao = int(input("Quantidade de pão: ")) * 0.5
quantidade_broa = int(input("Quantidade de broa: ")) * 1.5

total_arrecadado = quantidade_broa + quantidade_pao

quanto_guardar = total_arrecadado * 0.10

print(quantidade_pao, quantidade_broa, total_arrecadado)

