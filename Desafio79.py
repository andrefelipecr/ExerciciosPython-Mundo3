# Códigos ANSI para cores
VOLTA = "\033[A"
LIMPA = "\033[2K"
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA}--- Lista de Valores Únicos ---{RESET}')

num = []
ordem_crescente = []

quantidade = int(input(f'{YELLOW}Quantos valores você quer adicionar?{RESET} '))
    
for i in range(quantidade):
    while True: # Looping: usuário não poderá digitar o mesmo valor mais de uma vez
        num.append(int(input(f'{YELLOW}Digite o {i+1}º número:{RESET} ')))
        
        if num.count(num[i]) == 1:
            break
        else:
            print(VOLTA,LIMPA,VOLTA)
            print(f'O número {num[i]} já foi adicionado.{RED} Tente novamente.{RESET}')
            del(num[i])

ordem_crescente = sorted(num)

print(f'''{'-='*18}
{CYAN}Resultados finais:{RESET}
Você digitou os valores:''', *ordem_crescente, sep=' ')
