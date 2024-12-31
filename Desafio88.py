# Códigos ANSI para cores
VOLTA = "\033[A"
LIMPA = "\033[2K"
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA}{"-"*30}\n{"Simulador de Mega Sena":^30}\n{"-"*30}{RESET}')

# Importações
from time import sleep
from random import randint

jogos = int(input(f'{YELLOW}Quantos jogos você quer jogar?{RESET} '))

# Laço de repetição: executa a quantidade que o usuário escolher
for i in range(jogos):
    jogo = []
    print(f'{CYAN}Jogo {i+1}:{RESET}', end=' ')
    for _ in range(6): # Laço: Sorteia 6 números e coloca numa lista vazia
            while True: # Loop
                num = randint(1, 60)
                if num not in jogo: # Verifica se o número randomizado não repete na mesma lista
                     break
            jogo.append(num)
    print(sorted(jogo)) # Mostra cada jogo em ordem crescente
    sleep(1.5)