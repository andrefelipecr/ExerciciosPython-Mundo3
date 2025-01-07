# Códigos ANSI para cores
VOLTA = "\033[A"
LIMPA = "\033[2K"
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

cadastros = soma_idades = 0
lista_clientes = []
mulheres = []
acima_da_media = []

while True: 
    print('-='*15)
    nome = input(f'{YELLOW}Nome do cliente:{RESET} ')
    
    # Dicionário: Guarda dados de clientes
    clientes = {
        "nome": nome,
        "gênero": input(f'{YELLOW}Gênero [m/f]:{RESET} ').strip().lower()[0],
        "idade": int(input(f'{YELLOW}Idade de {nome}:{RESET} '))
    }
    
    cadastros += 1 # Contador de cadastros realizados
    
    # Lista: Guarda o nome das mulheres cadastradas
    if clientes["gênero"] == 'f':
        mulheres.append(clientes["nome"])
    
    soma_idades += clientes["idade"]
    
    lista_clientes.append(clientes) # Lista: Contêm um dicionário para cada cliente
    
    escolha = input(f'Continuar cadastrando clientes? [s/n]: ').strip().lower()[0]
    print(VOLTA,LIMPA,VOLTA)
    if escolha == 'n':
        break

media_idades = soma_idades / cadastros # Calcula a média de idades dos clientes

# Laço de repetição: Guarda pessoas acima da média em uma lista
for c in lista_clientes:
    if c["idade"] > media_idades:
        acima_da_media.append(c)

print('-='*15)
print(f'{CYAN}Resultados Finais:{RESET}')
print(f'A) Ao todo, {cadastros} clientes foram cadastrados.')
print(f'B) {media_idades} anos é a idade média dos clientes.')
print(f'C) As clientes mulheres são {", ".join(mulheres)}.')

if acima_da_media:
    print(f'D) Clientes com idade acima da média:')
    for cliente in acima_da_media:
        print(f'    >>> {cliente["nome"]}; idade = {cliente["idade"]} anos')
else:
    print(f'D) Nenhum cliente tem idade acima da média.')
print(f'{CYAN}<<Encerrado>> Volte sempre!{RESET}')
