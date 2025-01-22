# Códigos ANSI para cores
VOLTA = "\033[A"
LIMPA = "\033[2K"
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

# Função: Calcula a idade da pessoa e informa a situação de voto(obrigatório, facultativo ou negado)
def voto(nascimento):
    
    # Importação: escopo local
    from datetime import datetime
    
    ano_atual = datetime.now().year
    idade = ano_atual - nascimento
    
    print(f'Você tem {GREEN}{idade} anos{RESET} de idade!')
    
    # Estrutura condicional: Retorna situação eleitoral a partir da idade da pessoa
    if 70 > idade >= 18:
        return f'VOTO OBRIGATÓRIO. Se não votar, ficará em débito com a Justiça Eleitoral'
    elif 16 <= idade < 18:
        return f'VOTO FACULTATIVO. Você já pode tirar o seu título de eleitor.'
    elif idade >= 70:
        return f'VOTO FACULTATIVO. Você já cumpriu o seu papel de cidadão.'
    else:
        return f'NÃO VOTA. Em {18 - idade} anos, você poderá votar.'


# Programa principal
ano = int(input(f'{YELLOW}Informe o ano em que você nasceu:{RESET} '))
print(VOLTA,LIMPA,VOLTA) # Limpa a linha anterior

print('-'*85)
print(voto(ano)) # Mostra o retorno da função
print('-'*85)

