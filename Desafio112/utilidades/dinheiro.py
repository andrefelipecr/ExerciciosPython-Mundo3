from cores import *

def formatado(preço, show=False):
    preço = f'{GREEN}R${RESET}{preço:.2f}'
    preço = preço.replace('.', ',')
    
    if show:
        return f'{"Preço analisado:":20}{preço}'
    
    else:
        return preço


def dobro(preço):
    preço *= 2
    preço = formatado(preço)    
    return f'{"Dobro do preço:":20}{preço}'


def metade(preço):
    preço /= 2
    preço = formatado(preço)   
    return f'{"Metade do preço:":20}{preço}'


def ajuste(preço, percentual):
    if percentual <= 0:
        percentual = abs(percentual)
        desconto = preço * (1 - (percentual / 100))
        return f'{f"{percentual}% de desconto:":20}{formatado(desconto)}'
    
    elif percentual > 0:
        aumento = preço * (1 + (percentual / 100))
        return f'{f"{percentual}% de acréscimo:":20}{formatado(aumento)}'


def analise(preço, percentual):
    print('-'*30)
    print(f'{MAGENTA}Análise do Preço{RESET}'.center(40))
    print('-'*30)
    print(formatado(preço, True))
    print(dobro(preço))
    print(metade(preço))
    print(ajuste(preço, percentual))
    print('-'*30)
    