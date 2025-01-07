# Códigos ANSI para cores
VOLTA = "\033[A"
LIMPA = "\033[2K"
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA}--- Estatísticas do Jogador ---{RESET}')

jogador = {} # Dicionário
jogador['nome'] = input(f'{YELLOW}Nome do jogador:{RESET} ').strip()
jogador['jogos'] = int(input(f'{YELLOW}Quantidade de jogos:{RESET} '))
jogador["gols"] = []
jogador["total_gols"] = 0

# Laço: Guarda a quantidade de gols por jogos
for i in range(1, jogador["jogos"] + 1):
    gols = (int(input(f'{YELLOW}Gols marcados no {i}º jogo:{RESET} ')))
    jogador["gols"].append(gols) # Lista de gols dentro do dicionário
    jogador["total_gols"] += gols # Calcula a quantidade total de gols

print('-='*37)
print(jogador) # Exibe o dicionário
print('-='*37)

# Exibe as estatísticas finais
print(f'{CYAN}O jogador {jogador["nome"]} jogou {jogador["jogos"]} partidas:{RESET}')
for i , g in enumerate(jogador["gols"]):
    print(f'    >>> Na {i+ 1}ª partida, fez {g} gols;')
print(f'{CYAN}Totalizando {jogador["total_gols"]} gols em sua carreira.{RESET}')
