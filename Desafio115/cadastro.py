from cores import *
import os
from os import system
from Desafio115.interface import cabeçalho
from Desafio115.arquivo import ler_arquivo, salvar_cadastro

def cadastrar():
    """Registra um novo cadastro e salva no arquivo."""
    system('cls' if os.name == 'nt' else 'clear')
    cabeçalho('NOVO CADASTRO', MAGENTA)
    
    while True:
        try:
            nome = input(f'| {YELLOW}Nome:{RESET} ').strip().title()
            idade = int(input(f'| {YELLOW}Idade:{RESET} '))
            if not nome:
                print(f'{RED}O nome não pode estar vazio!{RESET}')
                continue
        except ValueError:
            print(f'{RED}Erro! Digite uma idade válida.{RESET}')
        else:
            salvar_cadastro('pessoas.txt', nome, idade)
            print('-'*40)
            print('|', f'{GREEN}Cadastro realizado com sucesso.{RESET}'.center(45), '|')
            print('-'*40)
            input(f'{CYAN}Pressione Enter para continuar...{RESET}')
            break

def ver_cadastros():
    """Exibe os cadastros salvos no arquivo."""
    system('cls' if os.name == 'nt' else 'clear')
    cabeçalho('PESSOAS CADASTRADAS', MAGENTA)
    cadastros = ler_arquivo('pessoas.txt')
    
    if not cadastros:
        print('|', f'{RED}Nenhuma pessoa cadastrada ainda.{RESET}'.center(45), '|')
    else:
        print(f'| {GREEN}Nome{" " * 26}Idade{RESET}  |')
        print('-'*40)
        for nome, idade in cadastros:
            print(f'| {nome:27} {idade:3} anos |')
    print('-'*40)
    input(f'{CYAN}Pressione Enter para continuar...{RESET}')
