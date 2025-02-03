from cores import *

def encontrar(txt):
    """Verifica se o arquivo existe."""
    try:
        with open(txt, 'rt'):
            return True
    except FileNotFoundError:
        return False

def criar_arquivo(txt):
    """Cria um arquivo caso ele não exista."""
    try:
        with open(txt, 'wt+') as arquivo:
            pass
    except Exception as e:
        print(f'{RED}Erro ao criar arquivo: {e}{RESET}')
    else:
        print(f'{GREEN}Arquivo <{txt}> criado com sucesso!{RESET}')

def ler_arquivo(txt):
    """Lê e retorna os cadastros do arquivo como uma lista de tuplas."""
    try:
        with open(txt, 'rt') as arquivo:
            return [tuple(linha.strip().split(';')) for linha in arquivo]
    except Exception as e:
        print(f'{RED}Erro ao ler o arquivo: {e}{RESET}')
        return []

def salvar_cadastro(txt, nome, idade):
    """Salva um novo cadastro no arquivo."""
    try:
        with open(txt, 'at') as arquivo:
            arquivo.write(f'{nome}; {idade}\n')
    except Exception as e:
        print(f'{RED}Erro ao salvar o cadastro: {e}{RESET}')

    