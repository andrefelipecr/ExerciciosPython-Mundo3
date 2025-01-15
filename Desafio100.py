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
from random import randint

# Função: Mostra o menu de opções e retorna escolha do usuário
def menu(titulo):
    print('-+'*20)
    print(f'{titulo:^50}')
    print('-'*40)
    print('1 - Somar Pares')
    print('2 - Somar Ímpares')
    print('3 - Sair')
    print('-+'*20)
    escolha = int(input(f'{YELLOW}Sua escolha:{RESET} '))
    return escolha


# Função: Sorteia 5 números entre 0 e 10 e guarda-os em uma lista
def sorteia():
    números = [randint(0, 10) for _ in range(5)]
    return números

# Função: Soma os números pares da lista
def soma_pares(números):
    S = 0
    S = sum(num for num in números if num % 2 == 0)
    print(f'\n{GREEN}A soma dos valores pares é {S}{MAGENTA}')


# Função: Soma os números ímpares da lista
def soma_ímpares(números):
    S = 0
    S = sum(num for num in números if num % 2 != 0)
    print(f'\n{MAGENTA}A soma dos valores ímpares é {S}{RESET}')


escolha = menu(f'{MAGENTA}MENU DE OPÇÕES{RESET}')

# Loop: Executa várias vezes o programa, até que o usuário escolha sair
while True:  
    system('cls') # Limpa Tela
    números = sorteia() # Recebe a lista dos valores sorteados
    escolha = menu(f'{CYAN}Números Sorteados: {números}{RESET}') # Recebe a escolha do usuário
    
    if escolha == 1:
        soma_pares(números)
    
    elif escolha == 2:
        soma_ímpares(números)
    
    elif escolha == 3: # Finaliza o programa
        print(f'{RED}Saindo do programa...{RESET}', end=' ', flush=True)
        sleep(1.5)
        print('Volte Sempre!')
        break
    
    else: # Mensagem de erro, se o usuário digitar um valor que não seja 1, 2 ou 3
        print(f'{RED}Opção inválida! Tente novamente.{RESET}')
        continue
    
    input(f'\n{YELLOW}Pressione Enter para continuar...{RESET}')
