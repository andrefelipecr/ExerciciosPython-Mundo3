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

# Função: recebe um comando digitado pelo usuário e exibe o manual do PyHelp sobre o comando
def ajuda(função):
    cabeçalho(f"MANUAL DO COMANDO '{comando}'", CYAN)
    help(função)


# Função: formata um cabeçalho para um título específico 
def cabeçalho(msg, cor):
    linhas = len(msg) + 2
    sleep(1)
    print(f'{cor}-{RESET}'*linhas)
    print(f' {cor}{msg}{RESET}')
    print(f'{cor}-{RESET}'*linhas)
    sleep(1)


# Programa principal
while True:
    cabeçalho('Sistema de Ajuda PyHelp', MAGENTA) # Título
    
    comando = input(f'{YELLOW}Função ou Biblioteca do Python >{GREEN} ').strip().lower()
    
    system('cls') # Limpa o terminal
    
    if comando == 'fim' or comando == 'sair': # Encerra o programa
        sleep(1)
        print(f'{RED}Saindo...{RESET}', end=' ', flush=True)
        sleep(1)
        print('VOLTE SEMPRE!')
        break
    
    ajuda(comando) # Chama a função
    sleep(1)
