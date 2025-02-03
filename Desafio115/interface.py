from cores import *
import os
from os import system

def cabeçalho(msg, cor):
    print('-'*40)
    print('|', f'{cor}{msg}{RESET}'.center(45), '|')
    print('-'*40)

def menu():
    system('cls' if os.name == 'nt' else 'clear')
    cabeçalho('MENU PRINCIPAL', MAGENTA)
    print(f'| 1 - Ver pessoas cadastradas          |')
    print(f'| 2 - Cadastrar nova pessoa            |')
    print(f'| 3 - Sair do sistema                  |')
    print('-'*40)
    
    while True:
        try:
            opcao = int(input(f'{YELLOW}Sua escolha:{RESET} '))
            if opcao not in [1, 2, 3]:
                print(f'{RED}Opção inválida! Escolha entre 1 e 3.{RESET}')
            else:
                return opcao
        except ValueError:
            print(f'{RED}Entrada inválida! Digite um número válido.{RESET}')

def sair():
    system('cls' if os.name == 'nt' else 'clear')
    cabeçalho('SAINDO DO SISTEMA... Volte sempre!', RED)
