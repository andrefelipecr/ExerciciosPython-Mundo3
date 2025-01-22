# Códigos ANSI para cores
VOLTA = "\033[A"
LIMPA = "\033[2K"
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"


# Função: Atente-se à docstring para entender com funciona a função
def análise(lista_notas, ver_aproveitamento=False):
    """
    Calcula e exibe dados de notas de uma turma.

    A função permite ao usuário inserir notas de alunos e exibe dados, 
    como o total de alunos, maior nota, menor nota, média das notas e aproveitamento geral.
    Caso o parâmetro `ver_aproveitamento` seja True, também exibe o aproveitamento da turma com base na média.

    Args:
        ver_aproveitamento (bool, opcional): Indica se o aproveitamento da turma deve ser exibido. 
                                    O padrão é False.

    Entrada do Usuário:
        O usuário insere as notas dos alunos e escolhe se deseja continuar adicionando mais notas.

    Exibe:
        - Total de alunos cadastrados.
        - Maior nota.
        - Menor nota.
        - Média da turma.
        - Aproveitamento (opcional): Indica se o aproveitamento é "BOM", "REGULAR" ou "RUIM", 
          com base na média da turma:
            * "BOM" se a média for maior ou igual a 7.
            * "REGULAR" se a média estiver entre 5 (inclusive) e 7.
            * "RUIM" se a média for menor que 5.

    Notas:
        O código utiliza constantes de cores (`YELLOW`, `GREEN`, `RED`, etc.) 
        para formatar a saída.

    Exemplo:
        >>> análise(lista_notas, ver_aproveitamento=False):
        Nota do 1º aluno: 8.5
        Continuar? s
        Nota do 2º aluno: 6.0
        Continuar? n

        -+-+-+-+-+-+-+-+-+-+-+-+-+
             DADOS DA TURMA:
        --------------------------
        Total de alunos:      2
        Maior nota:           8.5
        Menor nota:           6.0
        Média da turma:       7.2
        Aproveitamento geral: BOM
        -+-+-+-+-+-+-+-+-+-+-+-+-+
    """

    # Entrada de dados no dicionário
    dados = {}
    dados["notas"] = lista_notas
    dados["total"] = len(lista_notas)
    dados["média"] = sum(lista_notas) / dados["total"]
    dados["maior"] = max(lista_notas)
    dados["menor"] = min(lista_notas)
    
    # Exibe os resultados da turma
    print()
    print('-+'*13)
    print(f'      {CYAN}DADOS DA TURMA:{RESET}')
    print('-'*26)
    print(f'Total de alunos: {dados["total"]:>6}')
    print(f'Maior nota: {dados["maior"]:>13}')
    print(f'Menor nota: {dados["menor"]:>13}')
    print(f'Média da turma:    {dados["média"]:>6.1f}')

    # Opcional: exibe aproveitamento geral da turma
    if ver_aproveitamento:
        if dados["média"] >= 7:
            dados["aproveitamento"] = f'{GREEN}BOM{RESET}'
        elif 5 <= dados["média"] < 7:
            dados["aproveitamento"] = f'{YELLOW}REGULAR{RESET}'
        else:
            dados["aproveitamento"] = f'{RED}RUIM{RESET}'
        
        print(f'{MAGENTA}Aproveitamento geral:{RESET} {dados["aproveitamento"]}')
    print('-+'*13)


# Programa principal
i = 0
notas = []

# Laço: leitura das notas dos alunos
while True:
    i += 1
    
    notas.append(float(input(f'{YELLOW}Nota do {i}º aluno:{RESET} ')))
    
    continuar = input('Continuar? ').strip().lower()[0]
    print(VOLTA,LIMPA,VOLTA)
    
    if continuar == 'n': # Encerra laço
        break

pergunta = input('Deseja vizualizar aproveitamento geral? ').strip().lower()[0]
print(VOLTA,LIMPA,VOLTA)

aproveitamento = True if pergunta == 's' else False

análise(notas, aproveitamento) # Chama a função
