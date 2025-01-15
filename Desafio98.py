# Códigos ANSI para cores
VOLTA = "\033[A"
LIMPA = "\033[2K"
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

# Importações
from os import system
from time import sleep

# Função: mostra o menu de opções
def menu():
    print(f'\n   {"~"*35}')
    print(f'   {"|  Escolha uma das opções abaixo  |"}')
    print(f'   {"~"*35}')
    print(f'   |a) Contagem de 1 até 10 de 1 em 1|')
    print(f'   |b) Contagem de 10 até 0 de 2 em 2|')
    print(f'   |c) Personalizar contagem         |')
    print(f'   |d) Sair                          |')
    print(f'   {"~"*35}')


# Função: Contagem personalizada pelo usuário
def contador(i, f, p):
    system('cls') # Limpa o terminal

    
    if p == 0: # Se o usuário digitar passo 0, o programa considerará passo 1
        p = 1
    
    system('cls')
    print('-='*40)
    print(f"{CYAN}Contando de {i} até {f} de {abs(p)} em {abs(p)}:{RESET}")
    sleep(2)
    
    # Se o inicio for maior que o fim, fará uma contagem decrescente
    if i > f:
        if p > 0:
            p = -p
        f -= 1
    else:
        f += 1
        p = abs(p)
    
    # Laço: Mostra a contagem
    for c in range(i, f, p):
        print(c, end='... ', flush=True)
        sleep(0.5)
    print(f'\n{"-="*40}')


# Programa principal:
while True:
    menu()
    opção = input(f'   {YELLOW}Sua escolha:{RESET} ').strip().upper()
    
    if opção == 'A':
        contador(1, 10, 1)
    
    elif opção == 'B':
        contador(10, 0, 2)
    
    elif opção == 'C':
        system('cls')
        
        # Entrada de dados: guarda o início, fim e passo 
        inicio = int(input(f'Início da contagem: '))
        fim = int(input(f'Fim da contagem: '))
        passo = int(input(f'Passo da contagem: '))
        
        contador(inicio, fim, passo)
    
    elif opção == 'D': # Encerra o programa
        print(f'\n{RED}Saindo do Programa{RESET}. Volte sempre!')
        sleep(1.5)
        break
    
    if opção not in "ABCD": # Valida se o usuário escolheu uma opção disponível no menu
        system('cls') # Limpa o terminal
        continue
