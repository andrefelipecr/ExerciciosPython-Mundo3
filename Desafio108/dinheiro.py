def dobro(preço):
    return preço * 2


def metade(preço):
    return preço / 2


def formatar(preço):
    preço = f'R${preço:.2f}'
    preço = preço.replace('.', ',')
    return preço


def ajuste(preço, percentual):
    if percentual < 0:
        percentual = abs(percentual)
        desconto = preço * (1 - (percentual / 100))
        return f'Desconto de {percentual}%, temos {formatar(desconto)}' 
    elif percentual > 0:
        aumento = preço * (1 + (percentual / 100))
        return f'Aumento de {percentual}%, temos {formatar(aumento)}'
    else:
        return f'Sem ajustes, temos {formatar(preço)}'
    