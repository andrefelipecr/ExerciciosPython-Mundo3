# Códigos ANSI para cores
VOLTA = "\033[A"
LIMPA = "\033[2K"
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA}----- Análise de Matriz -----{RESET}')

soma_pares = soma_coluna = 0
linha2 = []
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] # Matriz 3x3

for l in range(3):
    for c in range(3):
        valores = int(input(f'{YELLOW}Digite um valor para [{l}, {c}]:{RESET} '))
        matriz[l][c] = valores
       
        if valores % 2 == 0: # Somatória dos valores pares da matriz
            soma_pares += valores
        if c == 2: # Somatória da 3ª coluna da matriz
            soma_coluna += valores
        if l == 1: # Guarda os valores da 2ª linha em uma lista
            linha2.append(valores)

print('-='*20, end='')

# Laço: mostra a matriz formatada
for l in range(3):
    print()
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end=' ')

print()
print('-='*20)

# Resultados das análises
print(f'''{CYAN}A){RESET} Soma dos valores pares da matriz: {soma_pares}
{CYAN}B){RESET} Soma da 3ª coluna da matriz: {soma_coluna}
{CYAN}C){RESET} Maior valor da 2ª linha: {max(linha2)}''')