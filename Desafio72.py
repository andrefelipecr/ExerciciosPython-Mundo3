# Códigos ANSI para cores
VOLTA = "\033[A"
LIMPA = "\033[2K"
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA}--- Número por Extenso ---{RESET}')

# Tupla: números de 0 até 20 por extenso
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
          'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
          'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

# Laço de repetição: usuário escolhe se quer ou não continuar
while True:
    # Laço de repetição: verifica se o usuário digitou um número entre 0 e 20
    while True:
        num = int(input(f'{YELLOW}Digite um número entre 0 e 20:{RESET} '))
        if 0 <= num <= 20:
            print(f'O número {num} por extenso é "{CYAN}{extenso[num]}{RESET}".')
            break
        else:
            print(VOLTA, LIMPA, VOLTA)
            print(f'{RED}Tente novamente.{RESET}', end=' ')
    
    escolha = input(f'{YELLOW}Quer continuar? [s/n]:{RESET} ').strip().upper()[0]
    print(VOLTA,LIMPA,VOLTA)
    
    if escolha == 'N':
        break
