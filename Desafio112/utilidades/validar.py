from cores import *
from os import system
import platform

def limpar_terminal():
    # Identifica o sistema operacional
    sistema = platform.system()
    system("cls") if sistema == "Windows" else system("clear")


def input_dinheiro(msg):
    while True:
        try:
            entrada = input(msg).replace(',', '.').strip()
            valor = float(entrada)
        except:
            print(f'{RED}Erro! O valor inserido não é um preço válido.{RESET}')
        else:
            limpar_terminal()
            return valor
