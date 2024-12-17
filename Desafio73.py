# Códigos ANSI para cores
VOLTA = "\033[A"
LIMPA = "\033[2K"
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'''{'-'*20}
| {MAGENTA}BRASILEIRÃO 2024{RESET} |
{'-'*20}''')

# Tupla: 20 times brasileiros
times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 'São Paulo',
        'Corinthians','Bahia', 'Cruzeiro', 'Vasco da Gama', 'Vitória', 'Atlético-MG', 'Fluminense',
        'Grêmio', 'Juventude','Bragantino', 'Atlético-PR', 'Criciúma', 'Atlético-GO', 'Cuiabá')

# Tupla em ordem alfabética 
ordem_times = sorted(times)

# Exibir tabela de classificação 
for i, tabela in enumerate(times):
    print(f'|{(i+1):2}º {tabela:14}|')

print(f'-'*20)

# Mostrar classificados para a Libertadores
print(f'{GREEN}Classificados para Copa Libertadores:{RESET} ', end='')
print(times[0:5])

# Mostra rebaixados
print(f'\n{RED}Rebaixados para segunda divisão:{RESET} ', end='')
print(times[-4:])

# Mostra times em ordem alfabética
print(f'\n{CYAN}Ordem alfabética:{RESET} ', end='')
for i in range(20):
    print(ordem_times[i], end='')
    print(end=', ') if i < 19 else print('.')

# Mostra a posição do time 'Flamengo'
print(f'\nO {GREEN}Palmeiras{RESET} está em {CYAN}{times.index("Palmeiras") + 1}º{RESET} lugar.')
