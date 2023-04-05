from utilidades.tools import *
from utilidades.operacoes import *
from time import sleep
#Para entender melhor as funções/ def -> Verifique em utilidades/operaoes 

while True:
    opc = menu(['Adição', 'Subtração', 'Divisão', 'Multiplicação', 'Mais opções...', 'Sair'])
    if opc == 1:
        titulo('Adição')
        quant = valInt(f'Quantos valores deseja somar?  ')
        print(f'{iadd(quant)}')
    elif opc == 2:
        titulo('Subtração')
        n1 = valInt(f'1º valor: ')
        n2 = valInt(f'2º valor: ')
        print(f'{n1} - {n2} = {sub(n1, n2)}')
    elif opc == 3:
        titulo('Divisão')
        n1 = valFloat('Valor do dividendo: ')
        n2 = valFloat('Valor do divisor: ')
        print(f'{n1} / {n2} = {division(n1, n2)}')
    elif opc == 4:
        titulo('Multiplicação')
        n1 = int(input('1º valor: '))
        n2 = int(input('2º valor: '))
        print(f'{n1} x {n2} = {multiply(n1, n2)}')
    elif opc == 5:
       opc = maisOpcao(['Sequencia de fibonacci', 'Progressão Aritimética', 'Fatorial'])
       if opc == 1:
           titulo('Sequência de Fibonacci')
           quant = int(input('Quantos termos deseja ver? '))
           print(fibonacci(quant))
       elif opc == 2:
           titulo('Progreção Aritimetica')
           quant = int(input('Quantos Termos deseja ver? '))
           termo = int(input('Primeiro termo: '))
           razao = int(input('Razão(pa): '))
           print(arithmetic(quant,termo,razao))
       elif opc == 3:
           titulo('Fatorial')
           fat = int(input('Digite o fatorial desejado: '))
           print(factorial(fat))
    else:
        if opc == 6:
            print('Saindo do programa...')
            break
    sleep(1)

    
