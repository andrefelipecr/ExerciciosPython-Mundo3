from Desafio108 import dinheiro
from cores import *

reais = float(input(f'{YELLOW}Insira o preço: {GREEN}R${RESET}'))

print(f'A metade de {dinheiro.formatar(reais)} é {dinheiro.formatar(dinheiro.metade(reais))}')
print(f'O dobro de {dinheiro.formatar(reais)} é {dinheiro.formatar(dinheiro.dobro(reais))}')
por_cento = int(input(f'{YELLOW}Digite o ajuste:{RESET} '))
limpa()
print(dinheiro.ajuste(reais, por_cento))