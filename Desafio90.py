# Códigos ANSI para cores
VOLTA = "\033[A"
LIMPA = "\033[2K"
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA}--- Dicionário: Status do aluno ---{RESET}')

dados = {} # Dicionário vazio

# Entrada de dados no dicionário
dados['Nome'] = input(f'{YELLOW}Nome do aluno: {RESET}')
dados['Média'] = float(input(f'{YELLOW}Média de {dados["Nome"]}:{RESET} '))
if dados['Média'] >= 7:
    dados["Status"] = f'{GREEN}Aprovado{RESET}'
elif  7 > dados["Média"] >= 5:
    dados["Status"] = f'{YELLOW}Em recuperação{RESET}'
else:
    dados['Status'] =f'{RED}Reprovado{RESET}'

# Mostra o conteúdo do dicionário
print('-'*25)
for k, v in dados.items():
    print(f'{k}: {v}')
print('-'*25)
