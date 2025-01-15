# Códigos ANSI para cores
VOLTA = "\033[A"
LIMPA = "\033[2K"
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

# Função: Cria um cabeçalho conforme o título que o usuário digitar
def cabeçalho(titulo):
    tamanho = len(titulo) + 4
    print('~'*tamanho)
    print(f'  {titulo}')
    print('~'*tamanho)


# Laço: Executa 3 vezes o comando abaixo
for _ in range(3):
    cabeçalho(input(f'\n{YELLOW}Digite o título:{RESET} ').strip().title()) # Chamada da função
