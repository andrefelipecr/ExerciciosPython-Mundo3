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
from time import sleep

print(f'{MAGENTA}--- Ordenador Automático de Lista ---{RESET}')

lista_valores = []

# Laço de repetição: Executa o bloco a seguir 5 vezes
for i in range(5):
    valor = int(input(f'{YELLOW}Digite o {i+1}º valor:{RESET} '))
    posiçao = 0
    
    # Compara o valor digitado com os  valores já presentes na lista
    while posiçao < len(lista_valores) and valor > lista_valores[posiçao]:
        posiçao += 1
    
    lista_valores.insert(posiçao,valor) # Insere o valor em uma lista, já na posição correta
    
    if valor == max(lista_valores):
        print(f'Adicionando {valor} ao final da lista...')
    else:
        print(f'Adicionando {valor} na posição {posiçao}...')
    
    sleep(2)
    print(VOLTA,LIMPA,VOLTA)

print('-='*19)
print(f'{CYAN}Lista final:{RESET} {lista_valores}')
