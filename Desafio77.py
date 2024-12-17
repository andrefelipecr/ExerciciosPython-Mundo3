# Códigos ANSI para cores
VOLTA = "\033[A"
LIMPA = "\033[2K"
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

# Entrada de dados: tupla e lista
palavras_tupla = ('Moletom', 'Estudar', 'Computador', 'Mouse', 'Arquivo',
                  'Teclado','Suco', 'Programador', 'Mundo', 'Python')
vogal = []

print(f'''{'-'*45}
| {MAGENTA}{'PALAVRAS':^15}{RESET} | {YELLOW}{'VOGAIS':^23}{RESET} |
{'-'*45}''')

# Laço de repetição: para cada palavra na tupla
for palavra in palavras_tupla:
    for letra in palavra.lower(): # Laço de reptição: para cada letra na palavra
        if letra in 'aeiou': # Estrutura condicional: analisa se cada letra é uma vogal
            vogal.append(letra) # Coloca as vogais de cada palavra na lista
    print(f'| {CYAN}{palavra:15}{RESET} | {GREEN}{", ".join(vogal):^23}{RESET} |')
    vogal = [] # Limpa a lista
print('-'*45)
