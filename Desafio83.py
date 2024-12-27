# Códigos ANSI para cores
VOLTA = "\033[A"
LIMPA = "\033[2K"
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA}--- Validação de Expressões ---{RESET}')

# Loop: Usuário escolhe se quer parar ou continuar
while True:
    contador = 0

    expressao = input(f'{YELLOW}Digite uma expressão:{RESET} ').strip().lower()
    
    # Laço de repetição: Separa cada termo(símbolo) da expressão 
    for termo in expressao:
        if termo == '(': # Ao abrir um parêntese, contador fica positivo
            contador += 1 
        elif termo == ')': # Ao fechar um parêntese, se já tiver um aberto, contador zera
            if contador > 0: 
                contador += -1
            else: # Ao fechar um parêntese antes de abrir, contador fica negativo
                contador += -1
                break
    
    # Estrutura condicional: verifica se os parênteses da expressão foram fechados corretamente
    if contador == 0:
        print(f'{GREEN}A expressão digitada está válida!{RESET}') 
    else:
        print(f'{RED}A expressão digitada está inválida!{RESET}')
    
    escolha = input('\nDeseja continuar validando expressões? [s/n]: ').strip().upper()[0]
    print(VOLTA,LIMPA,VOLTA)

    if escolha == 'N': # Encerra o loop
        break
