# Códigos ANSI para cores
VOLTA = "\033[A"
LIMPA = "\033[2K"
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA}--- Exercício Simples sobre Lista ---{RESET}')

valores = []
i = 0

# Laço de repetição: usuário digita quantos valores quiser
while True:
    valores.append(int(input(f'{YELLOW}{i + 1}º valor:{RESET} ')))
    i += 1
    
    escolha = input('Quer continuar? [s/n]: ').strip().upper()[0]
    print(VOLTA,LIMPA,VOLTA)

    if escolha == 'N': # Encerra o laço
        break

valores.sort(reverse=True) # Ordena lista em ordem decrescente

print(f'''{'-='*20}
{CYAN}A){RESET} Ao todo você digitou {i} valores.
{CYAN}B){RESET} Valores em ordem decrescente: {valores}''')

if 5 in valores:
    posiçao_5 = valores.index(5) + 1 # Posição em que o 5 aparece pela primeira vez na lista
    print(f'{CYAN}C){RESET} O valor 5 {GREEN}faz parte da lista!{RESET} Foi encontrado na {posiçao_5}ª posição')
else:
    print(f'{CYAN}C){RESET} O valor 5 {RED}não faz parte da lista!{RESET}')
    