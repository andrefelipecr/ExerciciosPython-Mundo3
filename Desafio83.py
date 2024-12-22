# Códigos ANSI para cores
VOLTA = "\033[A"
LIMPA = "\033[2K"
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA}--- Lista: Validação de Expressões ---{RESET}')

# Loop: Usuário escolhe se quer parar ou continuar
while True:
    lista_elementos = []

    expressao = input(f'{YELLOW}Digite uma expressão:{RESET} ').strip().lower()
    
    # Laço de repetição: Separa cada elemento da expressão em uma lista
    for c in range(len(expressao)):
        lista_elementos.append(expressao[c])
    
    # Estrutura condicional: verifica se os parênteses da expressão foram fechados corretamente
    if lista_elementos.count('(') == lista_elementos.count(')'):
        print(f'{GREEN}A expressão digitada está válida!{RESET}\n')
    else:
        print(f'{RED}A expressão digitada está inválida!{RESET}\n')
    
    escolha = input('Deseja continuar validando expressões? [s/n]: ').strip().upper()[0]
    print(VOLTA,LIMPA,VOLTA)

    if escolha == 'N': # Encerra o loop
        break
