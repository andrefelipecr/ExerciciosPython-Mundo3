# Códigos ANSI para cores
VOLTA = "\033[A"
LIMPA = "\033[2K"
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"


# Função: parâmetros opcionais
def jogador(n=f'{RED}<não informado>{RESET}', g=0):
    return f'O jogador {GREEN}{n}{RESET} fez {CYAN}{g} gol(s){RESET} em sua carreira.'


# Programa principal
nome = input(f'{YELLOW}Nome do jogador:{RESET} ').strip()
gols = input(f'{YELLOW}Gols marcados:{RESET} ').strip()

if not gols.isnumeric(): # Se usuário não digitar um número, considera 0 gols
    gols = 0

if nome == '': # Se deixar o nome em branco
    print(jogador(g=gols))
else:
    print(jogador(nome, gols))