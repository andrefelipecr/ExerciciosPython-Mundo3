from Desafio108.dinheiro import ajuste, dobro, formatar, metade
from cores import *

reais = float(input(f'{YELLOW}Insira o preço: {GREEN}R${RESET}'))

print(f'A metade de {formatar(reais)} é {formatar(metade(reais))}')
print(f'O dobro de {formatar(reais)} é {formatar(dobro(reais))}')
por_cento = int(input(f'{YELLOW}Digite o ajuste:{RESET} '))
limpa()
print(ajuste(reais, por_cento))