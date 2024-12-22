# Códigos ANSI para cores
VOLTA = "\033[A"
LIMPA = "\033[2K"
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA}--- Listas: Separador de Pares e Ímpares ---{RESET}')

valores_par = []
valores_impar = []
valores = []
i = 1

# Loop: Cria uma lista com vários valores digitados pelo usuário
while True:
    valores.append(int(input(f'{YELLOW}Digite o {i}º valor inteiro:{RESET} ')))
    i += 1
    
    escolha = input(f'Deseja continuar? [s/n]: ').strip().upper()[0]
    print(VOLTA,LIMPA,VOLTA)
    
    if escolha == 'N': # Encerra o loop
        print('-'*40)
        break

# Laço de repetição: Verifica se o valor digitado é par ou ímpar
for v in valores:
    if v != 0:
        if v % 2 == 0:
            valores_par.append(v)
        else:
            valores_impar.append(v)

print(f'{CYAN}Lista Completa:{RESET}',valores)
print(f'{CYAN}Valores pares:{RESET}', end=' ')
print(*valores_par, sep=', ')
print(f'{CYAN}Valores ímpares:{RESET}', end=' ')
print(*valores_impar, sep=', ')
