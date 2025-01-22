# Códigos ANSI para cores
VOLTA = "\033[A"
LIMPA = "\033[2K"
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"


# Função: Atente-se à docstring para entender como funciona esta função
def fatorial(num, equação):
    """
    Calcula o fatorial de um número e, opcionalmente, retorna a representação detalhada da equação.

    Parâmetros:
        num (int): O número inteiro para o qual será calculado o fatorial. Deve ser maior ou igual a 0.
        equação (bool): Se True, retorna a equação detalhada do cálculo do fatorial em formato de string. 
                        Se False, retorna apenas o valor do fatorial.

    Return:
        str: Uma string que contém o cálculo do fatorial no formato detalhado (se `equação` for True)
             ou apenas o resultado do fatorial. O resultado é formatado com as variáveis `GREEN` e `RESET`
             para estilização.

    Exemplos:
        >>> fatorial(5, True)
        '5 x 4 x 3 x 2 x 1 = \x1b[32m120\x1b[0m'
        >>> fatorial(5, False)
        '5! = \x1b[32m120\x1b[0m'
        >>> fatorial(0, False)
        '0! = \x1b[32m1\x1b[0m'

    Notas:
        - O cálculo considera que 0! = 1 por definição.
    """

    resultado = 1
    
    for n in range(num, 0, -1): # Laço: calcula o produto do número digitado até 1, ou seja, o fatorial
        resultado *= n
    
    if equação and 0 != num != 1: # Exibe equação completa 
        equação_str = " x ".join(str(n) for n in range(num, 0, -1))
        return f"{equação_str} = {GREEN}{resultado}{RESET}"
    else: # Exibe apenas o resultado
        return f'{num}! = {GREEN}{resultado}{RESET}'

       
print('-'*25)
numero = int(input(f'{CYAN:11}Fatorial de '))
print(RESET, end='')
print('-'*25)

mostrar = input(f'Vizualizar a equação completa de {numero} fatorial? ').strip().lower()[0]
print(VOLTA,LIMPA,VOLTA) # Limpa a linha anterior

resposta = True if mostrar == 's' else False

print(fatorial(numero, resposta)) # Mostra retorno da função
