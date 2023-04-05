from utilidades.tools import *
def iadd(quant = 2): #Soma qualquer quantidade de numeros que deseja
    '''
    diferente de otras funções soma,
    nessa é necessario apenas colocar a 
    quantidade de somas que deseja realizar
    no parametro: quant
    '''
    s = 0
    cont = 1
    while cont <= quant: 
        n = valInt(f'Digite o {cont}º valor: ') #Recebe os valores para somar
        s += n
        cont += 1
    return f'|Resultado da soma: {s}|' #Retorna o resultado


def sub(num1, num2): #Subtração de numeros inteiros
    s = num1 - num2
    return s #Retorna o resultado


def division(n1 = 0, n2 =0 ): #Divisão usando tratamento de erros
        try:
            d = n1 / n2
        except (ZeroDivisionError,TypeError):
            print('\033[0;31mValor não divisivel, tente novamente.\033[m')
        else:
            return f'{d:.2f}' #Retorna o resultado
    
    
def multiply(n1 ,n2):
    m = n1 * n2
    return m #Retorna o resultado


def arithmetic(quant, fterm, pa): #Expressão aritimetica - 
    razao = pa #razão
    termo = fterm # primeiro termo
    cont = 1
    while cont <= quant: #quant  = quantidade de termos que vai ser mostrado
        print(f'{termo}', end='')
        print(' -> ' if cont < quant else '', end='')
        termo += razao
        cont += 1
    print('.')


def factorial(fat):
    valor = fat 
    res = 1 # Pois o valor nulo de multiplicaçãp é igual a 1
    print(f'{valor}! = ', end='')
    for c in range(valor, 0, -1):
        print(f'{c}', end='')
        print(' x ' if c > 1 else ' = ', end='')
        res *= c
    return res
    
    
    
def fibonacci(quant): 
    t1 = 0 # T1 = 0 pois na sequencia de fibonacci o primerio termo sempre vai ser 0
    t2 = 1 # T1 = 0 pois na sequencia de fibonacci o segundo termo sempre vai ser 1
    print(f'{t1} -> {t2}', end='')
    cont = 3#Começa contando no 3
    while cont <= quant: #quant = quantidade de termos que serão exibidos 
        t3 = t1 + t2
        print(f' - > {t3}', end='')
        t1 = t2
        t2 = t3
        cont += 1
    print('.')
    

    
        

    