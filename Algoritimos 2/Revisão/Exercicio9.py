#Calculadora Simples com Menu
#Exiba um menu:
#1. Soma  
#2. Subtração  
#3. Multiplicação  
#4. Divisão  

#Leia a opção e dois números, então exiba o resultado.
#Repita até o usuário digitar "sair" (use while True).





# Dicionário que define o "mundo" seguro para o eval.
# A chave aqui é remover o acesso às funções perigosas embutidas.
safe_globals = {
    '__builtins__': None
}

# Loop infinito para manter a calculadora funcionando
while True:
    expressao = input("Digite a sua conta (ou 'sair' para fechar): ")

    if expressao.lower() == 'sair':
        print("Até a próxima!")
        break

    try:
        # A MÁGICA SEGURA!
        # Passamos nosso dicionário de 'globals' como segundo argumento.
        # Agora, o eval() só pode acessar o que está nesse dicionário (nada!).
        resultado = eval(expressao, safe_globals)
        print(f"O resultado é: {resultado}")

    # Este erro agora pode pegar tanto uma expressão matemática inválida
    # quanto uma tentativa de usar uma função proibida.
    except (NameError, TypeError, SyntaxError):
        print("Expressão inválida ou tentativa de usar uma função não permitida.")
    except Exception as e:
        # Pega qualquer outro erro inesperado
        print(f"Ocorreu um erro: {e}")