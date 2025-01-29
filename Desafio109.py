from Desafio109.dinheiro import ajuste, dobro, formatado, metade
from cores import *

reais = float(input(f'{YELLOW}Insira o preço: {GREEN}R${RESET}'))

print(f'A metade de {formatado(reais)} é {metade(reais, True)}')
print(f'O dobro de {formatado(reais)} é {dobro(reais, True)}')
por_cento = int(input(f'{YELLOW}Digite o ajuste:{RESET} '))
limpa()
print(ajuste(reais, por_cento, True))