from urllib import error
from urllib.request import urlopen
from webbrowser import open
from cores import *

def abrir_youtube(site):
    """
    Tenta acessar um site fornecido e oferece a opção de abri-lo no navegador.

    Parâmetros:
        site (str): A URL do site a ser acessado.

    Comportamento:
        - Verifica se o site está acessível.
        - Se o site não puder ser acessado, exibe uma mensagem de erro.
        - Se o site estiver acessível, solicita ao usuário se deseja abri-lo.
        - Se o usuário escolher "sim", tenta abrir o site no navegador.
        - Se o usuário escolher "não", exibe uma mensagem de despedida.

    Dependências:
        - `urlopen` e `error.URLError` da biblioteca `urllib.request`
        - `open` para abrir a URL no navegador
        - Variáveis de formatação de cores (`RED`, `GREEN`, `CYAN`, `RESET`)
        - Função `limpa()` (deve estar definida no código)

    Exemplo de uso:
        url = "https://youtube.com/"
        abrir_youtube(url)
    """
    try:
        abrir = urlopen(site)
    except error.URLError:
        print(f'{RED}Não foi possível acessar {site}{RESET}')
    else:
        print(f'{GREEN}O site <{site}> está acessível!{RESET}', end=' ')
        while True:
            escolha = input('Deseja abrí-lo? [sim/não]: ').strip().lower()
            limpa()

            if escolha == 'sim':
                open(site)
                break
            elif escolha == 'não':
                print(f'{CYAN}Obrigado e volte sempre!{RESET}')
                break


url = "https://youtube.com/"
abrir_youtube(url)
