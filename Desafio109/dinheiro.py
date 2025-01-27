def formatado(preço):
    preço = f'R${preço:.2f}'
    preço = preço.replace('.', ',')
    return preço


def dobro(preço, formatar):
    preço *= 2
    if formatar:
        preço = formatado(preço)
    return preço


def metade(preço, formatar):
    preço /= 2
    if formatar:
        preço = formatado(preço)
    return preço


def ajuste(preço, percentual, formatar):
    if percentual < 0:
        percentual = abs(percentual)
        
        desconto = preço * (1 - (percentual / 100))
        
        if formatar:
            desconto = formatado(desconto)
        
        return f'Desconto de {percentual}%, temos {desconto}' 
    
    elif percentual > 0:
        aumento = preço * (1 + (percentual / 100))
       
        if formatar:
            aumento = formatado(aumento)
        
        return f'Aumento de {percentual}%, temos {aumento}'
    
    else:
        if formatar:
            preço = formatado(preço)
        return f'Sem ajustes, temos {preço}'