# Códigos ANSI para cores
VOLTA = "\033[A"
LIMPA = "\033[2K"
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA}--- Analisando Valores de uma Tupla ---{RESET}')

lista_num = []
pares_num = []

# Laço de repetição: Lê 5 valores e coloca em uma lista
for i in range(1, 5):
    num = int(input(f'{YELLOW}Digite o {i}º valor:{RESET} '))
    lista_num.append(num)
    if num % 2 == 0:
        pares_num.append(num) # Lista dos valores pares

# Analisa quantas vezes o número 9 foi digitado
if lista_num.count(9) == 0:
    print(f'\n{CYAN}a){RESET} O número 9 não apareceu nenhuma vez.')
else:
    print(f'\n{CYAN}a){RESET} O número 9 apareceu {lista_num.count(9)} vez(es).')

# Analisa se o número 3 foi digitado e em qual posição
if 3 not in lista_num:
    print(f'{CYAN}b){RESET} O número 3 não foi digitado em nenhuma posição.')
else:
    print(f'{CYAN}b){RESET} O número 3 apareceu na {lista_num.index(3) + 1}ª posição.')

# Analisa os números pares digitados
if pares_num == []:
    print(f'{CYAN}c){RESET} Nenhum valor par foi digitado.')
else:
    print(f'{CYAN}c){RESET} Quais foram os números pares: {pares_num}.')
