# Códigos ANSI para cores
VOLTA = "\033[A"
LIMPA = "\033[2K"
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"


# Função: validação de erros
def inteiro():
    try: # Tentar ler número inteiro
        num = int(input(f'{YELLOW}Digite um número inteiro:{RESET} '))
        print(VOLTA,LIMPA,VOLTA)
    
    except: # Se houver erros, mostra mensagem de erro
        print(f'{RED}ERRO!{RESET} Você deve digitar um número inteiro para continuar.')
    
    else: # Se não houver erros, retorna o número digitado
        return num
    print('-+'*29)


# Programa principal
print(f'{MAGENTA}------------------- Validação Simples -------------------{RESET}')

while True: # Laço: enquanto o usuário não digitar um número, repete a função
    número = inteiro()
    
    if número: # Se a função retornar o número, encerra o laço 
        print(f'{GREEN}Você acabou de digitar o número {número}!{RESET}'.center(68))
        break
