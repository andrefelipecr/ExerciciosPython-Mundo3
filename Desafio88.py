# Códigos ANSI para cores
VOLTA = "\033[A"
LIMPA = "\033[2K"
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA}{"-"*30}\n{"Simulador de Mega da Virada":^30}\n{"-"*30}{RESET}')

# Importações
from time import sleep
from random import sample

# Laço de repetição: executa a quantidade que o usuário escolher
for i in range(int(input(f'{YELLOW}Quantos jogos você quer jogar?{RESET} '))):
    print(f'{CYAN}Jogo {i+1}:{RESET}', end=' ')
    palpites = sample(range(61), 6) # Sorteia, aleatóriamente, 6 números entre 0 e 60 sem repetições
    print(sorted(palpites)) # Mostra os palpites em ordem crescente
    sleep(1.5)
print(f'{GREEN:<15}BOA SORTE!!{RESET}')