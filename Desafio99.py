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

# Função: Desempacotamento de parâmetro: recebe valores aleatórios e mostra qual foi o maior
def maior(*valores):
    print('+-'*24)
    print(f'{MAGENTA}Analisando Valores...{RESET}', end=' ', flush=True)
    sleep(1)
    print(', '.join(map(str, *valores)))
    sleep(1)
    if len(*valores) != 0:
        print(f'Foram informados {len(*valores)} valores, sendo {max(*valores)} o maior.')
    else:
        print(f'{RED}Nenhum valor foi informado.{RESET}')
    print('+-'*24)

lista = []

for quantidade in range(randint(0, 6)): # Executa o comando abaixo de 0 a 6 vezes
    lista.append(randint(0, 10)) # Sorteia valor aleatório e guarda em uma lista

maior(lista)
