from Desafio112.utilidades import dinheiro, validar
from cores import *

reais = validar.input_dinheiro(f'{YELLOW}Insira o preço: {GREEN}R${RESET}')
por_cento = int(input(f'{YELLOW}Digite o acréscimo ou o desconto:{RESET} '))
limpa()
dinheiro.analise(reais, por_cento)
