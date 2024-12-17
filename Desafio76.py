# Códigos ANSI para cores
VOLTA = "\033[A"
LIMPA = "\033[2K"
RESET = "\033[0m"
RED = "\033[31m"
MAGENTA = "\033[35m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"

print(f'''{'-'*30}
|{MAGENTA:9}LISTAGEM DE PRODUTOS{RESET:8}|
{'-'*30}''')

# Tupla: produtos e preços
produtos = ('Notebook', 2500, 'PS5', 4500, 'Smartwatch', 800, 'Livro', 34.90, 'Hambúrguer', 28.90, 'Suco natural', 8.50)

print(f"|{'Produto':^14}|{'Preço':^13}|")
print('-'*30)

# Laço de repetição: mostra os produtos e preços de forma tabular
for i in range(0, len(produtos), 2):
    print(f'{produtos[i]:20} R${produtos[i+1]:7.2f}')
print('-'*30)
