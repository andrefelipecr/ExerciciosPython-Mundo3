from cores import *

def inteiro():
    while True:
        try:
            num = int(input(f'{YELLOW}Digite um número inteiro:{RESET} '))
            print(VOLTA,LIMPA,VOLTA)
        
        except:
            print(f'{RED}ERRO!{RESET} Você deve digitar um número inteiro para continuar.')
        
        else:
            return num
        print('-+'*29)


def real():
    while True:
        try:
            entrada = input(f'{YELLOW}Digite um número real:{RESET} ').strip().replace(',', '.')
            num = float(entrada)
            print(VOLTA,LIMPA,VOLTA)
        
        except:
            print(f'{RED}ERRO!{RESET} Você deve digitar um número real para continuar.')
        
        else:
            return num
        print('-+'*29)

print(f'{GREEN}Você acabou de digitar os números {inteiro()} e {real()}{RESET}'.center(68))
