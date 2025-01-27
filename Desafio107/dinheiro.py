def dobro(preço):
    return preço * 2


def metade(preço):
    return preço / 2


def ajuste(preço, percentual):
    if percentual < 0:
        percentual = abs(percentual)
        return f'Desconto de {percentual}%, temos R${preço * (1 - (percentual / 100)):.2f}' 
    elif percentual > 0:
        return f'Aumento de {percentual}%, temos R${preço * (1 + (percentual / 100)):.2f}'
    else:
        return f'Sem ajustes, temos R${preço}'
