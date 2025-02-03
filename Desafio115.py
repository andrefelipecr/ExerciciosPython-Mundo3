from Desafio115.interface import menu, sair
from Desafio115.cadastro import cadastrar, ver_cadastros
from Desafio115.arquivo import *

arquivo = 'pessoas.txt'

if not encontrar(arquivo):
    criar_arquivo(arquivo)

while True:
    opção = menu()
    if opção == 1:
        ver_cadastros()
    elif opção == 2:
        cadastrar()
    elif opção == 3:
        sair()
        break

