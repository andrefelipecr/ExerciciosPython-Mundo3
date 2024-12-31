# Códigos ANSI para cores
VOLTA = "\033[A"
LIMPA = "\033[2K"
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'{MAGENTA}--- Boletim de Notas ---{RESET}')

# Lista composta: nome, nota 1, nota 2 e média das notas
aluno = [[], [], [], []]

# Laço de repetição
while True:
    nome = input(f'{YELLOW}Nome do(a) estudante: {RESET}')
    aluno[0].append(nome)
    
    nota1 = float(input(f'1ª nota: '))
    aluno[1].append(nota1)
    
    nota2 = float(input(f'2ª nota: '))
    aluno[2].append(nota2)
    
    media = (nota1 + nota2) / 2
    aluno[3].append(media)
    
    escolha = input('Continuar cadastrando? [s/n]: ').strip().upper()[0]
    print(VOLTA,LIMPA,VOLTA)
    if escolha == 'N': # Encerra o laço
        break
print('-='*16)
print(f'{"    NOME":20}{"MÉDIA"}\n{"-"*32}')
for i in range(len(aluno[0])): # Mostra tabela de alunos cadastrados e suas respectivas médias
    cor = GREEN if aluno[3][i] >= 7 else RED
    print(f'{CYAN}{i}{RESET}   {aluno[0][i]:18}{cor}{aluno[3][i]:.1f}{RESET}')

while True: # Loop
    print('-='*16)
    posiçao = int(input(f'Analisar notas de qual aluno? [999 para sair]: '))
    print(VOLTA,LIMPA,VOLTA)
    if posiçao == 999: # Encerra o programa
        print(f'{CYAN}Programa finalizado... Volte sempre!{RESET}')
        break
    else: # Mostra notas do aluno escolhido pelo usuário
        print(f'Notas de {aluno[0][posiçao]} foram {aluno[1][posiçao]}, {aluno[2][posiçao]}')