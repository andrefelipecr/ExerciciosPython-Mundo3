from Desafio109 import dinheiro
from cores import *

reais = float(input(f'{YELLOW}Insira o preço: {GREEN}R${RESET}'))

print(f'A metade de {dinheiro.formatado(reais)} é {dinheiro.metade(reais, True)}')
print(f'O dobro de {dinheiro.formatado(reais)} é {dinheiro.dobro(reais, True)}')
por_cento = int(input(f'{YELLOW}Digite o ajuste:{RESET} '))
limpa()
print(dinheiro.ajuste(reais, por_cento, True))