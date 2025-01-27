from Desafio107 import dinheiro
from cores import *

reais = float(input(f'{YELLOW}Insira o preço: {GREEN}R${RESET}'))

print(f'A metade de R${reais:.2f} é R${dinheiro.metade(reais):.2f}')
print(f'O dobro de R${reais:.2f} é R${dinheiro.dobro(reais):.2f}')
por_cento = int(input(f'{YELLOW}Digite o ajuste:{RESET} '))
limpa()
print(dinheiro.ajuste(reais, por_cento))