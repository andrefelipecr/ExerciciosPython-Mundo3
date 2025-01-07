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
from random import randint
from time import sleep

print('-'*52)
print(f'Quatro jogadores irão decidir quem começará a rodada')
print('-'*52)
sleep(1.5)
print(f'Joguem os dados!')
sleep(1)

# Dicionário: cada jogador recebe um número aleatório entre 1 e 6
sorteio = {
    f'{RED}jogador vermelho{RESET}': randint(1, 6),
    f'{MAGENTA}jogador magenta {RESET}': randint(1, 6),
    f'{GREEN}jogador verde   {RESET}': randint(1, 6),
    f'{YELLOW}jogador amarelo {RESET}': randint(1, 6)
    }

# Laço: mostra os resultados do sorteio
for k, v in sorteio.items():
    print(f'   O {k} tirou {v}')
    sleep(1)

print('\nOrdem dos jogadores:')
i = 1

# Laço: ordena os jogadores pelos números sorteados e exibe a ordem decrescente
for k, v in sorted(sorteio.items(), key=lambda item: item[1], reverse=True):
    print(f'   {i}º lugar: {k} com {v}')
    sleep(1)
    i += 1
    