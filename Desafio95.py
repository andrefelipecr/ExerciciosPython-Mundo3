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

lista_jogadores = []

# Loop: cadastro de nomes, quantidade de partidas e gols
while True:
    nome = input(f'{YELLOW}Nome do jogador:{RESET} ').strip()
    
    # Dicionário: dados do jogador
    jogador = { 
        "nome": nome,
        "jogos": int(input(f'{YELLOW}Quantidade de jogos de {nome}:{RESET} ')),
        "gols": [],
        "total_gols": 0
    }
    
    # Laço: Guarda a quantidade de gols por jogos
    for i in range(1, jogador["jogos"] + 1):
        gols = (int(input(f'{YELLOW}Gols marcados no {i}º jogo:{RESET} ')))
        jogador["gols"].append(gols) # Lista de gols dentro do dicionário
        jogador["total_gols"] += gols # Calcula a quantidade total de gols
    
    lista_jogadores.append(jogador) # Lista: Guarda todos os jogadores e seus dados

    print('-'*42)
    
    escolha = input(f'Quer continuar? [s/n]: ').strip().lower()[0]
    print(VOLTA,LIMPA,VOLTA)
    if escolha == "n": # Encerra o loop
        break

print(f"     {'Nome':15}{'Gols':15}{'Total'}\n{'-'*42}")

# Laço: Tabela de jogadores cadastrados
for i, j in enumerate(lista_jogadores):
    print(f'   {i} {str(j["nome"]):15}{str(j["gols"]):15}{j["total_gols"]}')
print('-'*42)

# Loop: Exibe os dados dos jogadores que o usuário escolher
while True:
    indice = int(input(f'Mostrar dados de qual jogador? [999 sair]: '))
    print(VOLTA,LIMPA,VOLTA)
    
    if 0 <= indice < len(lista_jogadores): # Mostra levantamento do jogador escolhido
        print(f'{CYAN}O jogador {lista_jogadores[indice]["nome"]} jogou {lista_jogadores[indice]["jogos"]} partidas:{RESET}')
        for i , g in enumerate(lista_jogadores[indice]["gols"]):
            print(f'    >>> Na {i+ 1}ª partida, fez {g} gols;')
    elif indice == 999: # Encerra o loop
        print(f'{GREEN}Programa finalizado. Volte sempre!{RESET}')
        break  
    else:
        print(f'{RED}ERRO!{RESET} Não existe jogador no índice {indice}. Tente novamente.') 
    print('-'*42)
    