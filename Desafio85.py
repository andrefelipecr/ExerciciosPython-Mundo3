# Códigos ANSI para cores
VOLTA = "\033[A"
LIMPA = "\033[2K"
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA}--- Lista Composta: Pares e Ímpares ---{RESET}')

valores = [[], []] # Lista com outras 2 listas imbutidas

# Laço: usuário irá digitar 7 valores inteiros
for i in range(1,8):
    valores.append(int(input(f'{YELLOW}Digite o {i}º valor:{RESET} ')))
    
    if valores[-1] % 2 == 0: # Se o valor for PAR, entrará na lista[0]
        valores[0].append(valores[-1])
    else: # Se o valor for ÍMPAR, entrará na lista[1]
        valores[1].append(valores[-1])

valores[0].sort() # Lista de pares em ordem crescente
valores[1].sort() # Lista de ímpares em ordem crescente

print(f'{"--"*25}\nOs valores pares digitados foram:', end=' ')
print(*valores[0], sep=', ')

print('Os valores ímpares digitados foram:', end=' ')
print(*valores[1], sep=', ')
