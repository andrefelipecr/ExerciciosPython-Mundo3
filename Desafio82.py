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

print(f'{CYAN}Lista Completa:{RESET}',valores)
print(f'{CYAN}Valores pares:{RESET}', end=' ')
print(f'{[pares for pares in valores if pares % 2 == 0 and pares != 0]}') # Laço Compacto: mostra pares
print(f'{CYAN}Valores ímpares:{RESET}', end=' ')
print(f'{[impares for impares in valores if impares % 2 == 1]}') # Laço compacto: mostra ímpares
