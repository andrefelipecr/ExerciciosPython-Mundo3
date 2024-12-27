# Códigos ANSI para cores
VOLTA = "\033[A"
LIMPA = "\033[2K"
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA:>13}--- Listas Compostas ---{RESET}')

cadastros = 0
nome = []
peso = []
pesados = []
leves = []

# Loop: Usuário escolhe se quer parar ou continuar
while True:
    print(f'-'*40)
    
    nome.append(input(f'Digite o nome: ')) # Lista de nomes digitados pelo usuário
    peso.append(float(input(f'Informe o peso de {nome[-1]}: '))) # Lista de pesos dos nomes cadastrados
    
    cadastros += 1 # Contador: Calcula a quantidade de cadastros
    
    escolha = input('Deseja continuar? [s/n]: ').strip().upper()[0]
    print(VOLTA,LIMPA,VOLTA)
    
    if escolha == 'N': # Encerra o loop
        break

peso_maior = max(peso) # Variável: maior peso digitado
peso_menor = min(peso) # Variável: menor peso digitado

for i, p in enumerate(peso):
    if p == peso_maior: # Se o peso for o maior de todos
        pesados.append(nome[i]) # Lista de nomes de quem possui o maior peso
    
    if p == peso_menor: # Se o peso for o menor de todos
        leves.append(nome[i]) # Lista de nomes de quem possui o menor peso
            
print('-'*40)
print(f'{MAGENTA}{cadastros:>6} cadastros feitos com sucesso{RESET}')
print(f'{CYAN}Maior Peso: {peso_maior}Kg{RESET}')
print(f'Pessoa(s) com maior peso: {GREEN}{", ".join(pesados)}{RESET}')
print(f'{YELLOW}Menor Peso: {peso_menor}Kg{RESET}')
print(f'Pessoa(s) com menor peso: {RED}{", ".join(leves)}{RESET}')
print('-'*40)
