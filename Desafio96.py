# Códigos ANSI para cores
VOLTA = "\033[A"
LIMPA = "\033[2K"
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

# Importações: system('cls') limpa o terminal, para sistema operacional Windows
from os import system

lista_áreas = []

# Função: calcula e mostra a área do terreno analisado
def área(l, c):
    print('-'*35)
    a = l * c
    lista_áreas.append(a)
# Vizualização das dimensões do terreno formatada
    print("        ┌" + "─" *10 + "┐")
    print(f"{l:5} m │" + " " *10 + "│")
    print("        └" + "─" *10 + "┘")
    print(f'{c:>15} m')
    print(f'A área do terreno é de {CYAN}{a:.1f} m²{RESET}.')
    print('-'*35)

# Função: menu de opções
def opções():
    escolha = int(input(f'''    {"-"*35}
    {MAGENTA}Escolha uma das opções:{RESET}
    1 - Controle de Terrenos
    2 - Vizualizar áreas calculadas
    3 - Sair
    {"-"*35}
    {YELLOW}Sua escolha:{RESET} '''))
    system('cls')
    return escolha # retorna o valor escolhido pelo usuário para o programa local


# Programa principal
while True:
    escolha = opções()
    
    if escolha == 1: # Lê largura e comprimento para calcular a área
        print(f'{MAGENTA}--------- Cálculo de Área ---------{RESET}')
        largura = float(input(f'{YELLOW}Largura do terreno em metros: {RESET}'))
        comprimento = float(input(f'{YELLOW}Comprimento do terreno em metros: {RESET}'))
        system('cls')
        área(largura, comprimento)

    if escolha == 2: # Mostra as áreas calculadas anteriormente
        print(f'{MAGENTA}---- Últimas Áreas Calculadas ----{RESET}')
        print(", ".join(f'{v:.1f} m²' for v in lista_áreas))
        print('-'*34)
    
    if escolha == 3: # Finaliza o programa
        print(f'{RED}Programa finalizado.{RESET} Volte Sempre!')
        break