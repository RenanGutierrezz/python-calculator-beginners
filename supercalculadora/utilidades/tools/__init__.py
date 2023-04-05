import os
def valInt(num): #Validação de inteiros
    try:
        numero = int(input(num))
    except (ValueError, TypeError):
        print(f'\033[0;31mERRO! VALOR INVÁLIDO!\033[m')
    else:
        return numero
    

def valFloat(num): #Validação de float
    try:
        numero = float(input(num))
    except (ValueError, TypeError):
        print(f'\033[0;31mERRO! VALOR INVÁLIDO!\033[m')
    else:
        return numero
    

def linha(txt = 32): #Cria linhas com 32 espaçoes de caracteres
    return '-' * txt


def coluna(txt = 1): #*IGNORAR* - Tentativa de criar uma coluna
    return '|' * txt


def titulo(txt): #Cria um "cabeçalho" formatado 
    print(linha())
    print(f'{coluna():<}{txt.center(30)}{coluna():>}')
    print(linha())
    
    
    
def menu(lista): #Cria um MENU principal apartir de uma lista
    titulo('MENU PRINCIPAL')
    c = 1
    for i in lista: #Serve para formatar/desempacotar a lista com as opções para o menu
        print(f'[{c}] - {i}') #Mostra as opções do menu 
        c += 1
    print(linha())
    opc = valInt('Escolha uma opção: ') #Realiza a escolha das opções da lista/menu
    os.system("cls") #Limpa o terminal logo após selecionar a opção
    return opc #Retorna a opção desejada
    

def maisOpcao(lista): #Cria um segundo menu secundario apartir de uma lista
    titulo('MATEMÁTICA "AVANÇADA"')
    c = 1
    for i in lista: #Serve para formatar/desempacotar a lista com as opções para o menu
        print(f'[{c}] - {i}') #Mostra as opções do menu 
        c += 1
    print(linha())
    opc = valInt('Escolha uma opção: ') #Realiza a escolha das opções da lista/menu
    os.system("cls") #Limpa o terminal logo após selecionar a opção
    return opc #Retorna a opção desejada
    