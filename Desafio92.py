# Códigos ANSI para cores
VOLTA = "\033[A"
LIMPA = "\033[2K"
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

from datetime import datetime

print(f'{MAGENTA}--- Tratamento de Dados com Dicionário ---{RESET}')
dados = {}
dados['nome'] = input(f'{YELLOW}Nome completo:{RESET} ').strip().title().split()[0]
dados['idade'] = - int(input(f'{YELLOW}Ano de nascimento:{RESET} ')) + datetime.now().year
dados['CTPS'] = int(input(f'{YELLOW}Carteira de trabalho [Se não tiver, digite 0]:{RESET} '))
if dados['CTPS'] != 0:
    dados['contratação'] = int(input(f'{YELLOW}Ano de contratação:{RESET} '))
    dados['salário'] = float(input(f'{YELLOW}Salário atual:{RESET} R$ '))
    dados['aposentadoria'] = dados['contratação'] - datetime.now().year + dados['idade'] + 35
print('-='*23)
print(f'{CYAN}Resultados Finais:{RESET}')
for k ,v in dados.items():
    print(f'  - {k} tem o valor {v}')
    