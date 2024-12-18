# Códigos ANSI para cores
VOLTA = "\033[A"
LIMPA = "\033[2K"
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA}--- Analisando Valores em uma Lista ---{RESET}')

# Lista vazia
num = []
posiçao_maior = []
posiçao_menor = []

# Laço de repetição: executa 5 vezes os comandos abaixo
for i in range(5):
    num.append(int(input(f'{YELLOW}Digite o {i+1}º valor:{RESET} '))) # Entrada de números em uma lista

for i, n in enumerate(num):
    if n == max(num):
        posiçao_maior.append(i+1) # Lista de posições do maior valor
    if n == min(num):
        posiçao_menor.append(i+1) # Lista de posições do menor valor


print(f'''{'-'*30}
{CYAN}Resultados finais:{RESET} {num}
{GREEN}O maior valor _{max(num)}_ foi encontrado na(s) {posiçao_maior}ª posição(ões){RESET}
{RED}O menor valor _{min(num)}_ foi encontrado na(s) {posiçao_menor}ª posição(ões){RESET}''')
