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

# Loop principal: cadastra dados de várias pessoas até que o usuário escolha parar
while True: 
    print('-='*15)
    
    nome = input(f'{YELLOW}Nome do cliente:{RESET} ')
    
    while True:
        gênero = input(f'{YELLOW}Gênero [m/f]:{RESET} ').strip().lower()[0]
        if gênero not in 'mf': # Validação de erro
            print(VOLTA,LIMPA,VOLTA)
            print(f'{RED}Inválido!{RESET} Digite apenas M ou F.')
        else:
            break
    
    # Dicionário: Guarda dados de clientes
    clientes = {
        "nome": nome,
        "gênero": gênero,
        "idade": int(input(f'{YELLOW}Idade de {nome}:{RESET} '))
    }
    
    cadastros += 1 # Contador de cadastros realizados
    
    # Lista: Guarda o nome das mulheres cadastradas
    if clientes["gênero"] == 'f':
        mulheres.append(clientes["nome"])
    
    soma_idades += clientes["idade"]
    
    lista_clientes.append(clientes) # Lista: Contêm um dicionário para cada cliente
    
    # Loop: valida se o usuário respondeu, corretamente, a pergunta
    while True:
        escolha = input(f'Continuar cadastrando clientes? [s/n]: ').strip().lower()[0]
        print(VOLTA,LIMPA,VOLTA)
        if escolha not in 'sn': # Validação de erro
            print(f'{RED}Inválido!{RESET} Responda apenas S ou N.')
        else: # Encerra o loop
            break
    
    if escolha == 'n': # Encerra o loop principal
        break

media_idades = soma_idades / cadastros # Calcula a média de idades dos clientes

# Laço de repetição: Guarda pessoas acima da média em uma lista
for c in lista_clientes:
    if c["idade"] > media_idades:
        acima_da_media.append(c)

print('-='*15)
print(f'{CYAN}Resultados Finais:{RESET}')
print(f'A) Ao todo, {cadastros} clientes foram cadastrados.')
print(f'B) {media_idades:.2f} anos é a idade média dos clientes.')

if mulheres: # Verifica se há mulheres na lista
    print(f'C) As clientes mulheres são {", ".join(mulheres)}.')
else:
    print(f'C) Nenhuma cliente mulher foi cadastrada.')

if acima_da_media: # Verifica se há pessoas com idades acima da média
    print(f'D) Clientes com idade acima da média:')
    for cliente in acima_da_media:
        print(f'    >>> {cliente["nome"]}; idade = {cliente["idade"]} anos')
else:
    print(f'D) Nenhum cliente tem idade acima da média.')
print(f'{CYAN}<<Encerrado>> Volte sempre!{RESET}')
