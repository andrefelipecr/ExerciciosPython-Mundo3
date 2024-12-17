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
from random import randint
from time import sleep

print(f'{MAGENTA}--- Maior e Menor de Listas Aleatórias ---{RESET}')

valores = []

# Laço de repetição: encerra quando usuário responder 'n'
while True:    
    for i in range(4): # Laço de repetição: executa 4 vezes o comando abaixo
        valores += [randint(1, 10)] # Atribui valores aleatórios a uma lista
    
    print(f'''      {valores} 
    O {CYAN}maior{RESET} valor foi {GREEN}{max(valores)}{RESET}
    O {CYAN}menor{RESET} valor foi {RED}{min(valores)}{RESET}''')
    
    escolha = input(f'{YELLOW}Quer continuar? [s/n]:{RESET} ').strip().upper()[0] # Lê escolha do usuário
    
    # Estrutura Condicional: Sai do looping se escolha for 'n', caso contrário, reinicia
    if escolha == 'N':
        print(f'{RED}Saindo...{RESET}')
        sleep(1.5)
        print(VOLTA,LIMPA,VOLTA)
        print(f'{CYAN}Obrigado por testar nosso programa. Volte sempre!{RESET}')
        break
    else:
        valores = []
        print(VOLTA,LIMPA,VOLTA)
