# Códigos ANSI para cores
VOLTA = "\033[A"
LIMPA = "\033[2K"
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA}------- Matriz 3x3 -------{RESET}')

# Matriz: 3 linhas e 3 colunas
matriz = [[[], [], []],
          [[], [], []],
          [[], [], []]]

# Laço de repetição: atribui valores para cada slot dentro da matriz
for l in range(3):
    for c in range(3):
        matriz[l][c].append(int(input(f'{YELLOW}Digite um valor para [{l}, {c}]:{RESET} ')))

print(f'{"-="*20}\n{CYAN}Resultado Final:{RESET}', end='')

# Laço de repetição: Mostra a matriz formatada
for l in range(3):
    print()
    for c in range(3):
        print('[ ',*matriz[l][c], end='  ] ')