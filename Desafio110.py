from Desafio110 import dinheiro
from cores import *

reais = float(input(f'{YELLOW}Insira o preço: {GREEN}R${RESET}'))
limpa()
por_cento = int(input(f'{YELLOW}Digite o acréscimo ou o desconto:{RESET} '))
limpa()
dinheiro.analise(reais, por_cento)