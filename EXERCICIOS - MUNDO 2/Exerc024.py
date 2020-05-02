numero1 = int(input('Digite o 1º Número: '))
numero2 = int(input('Digite o 2º Número: '))
opcao = 1

while opcao != 5:
    print('''
    ------------------------------
    [ 1 ] - Somar                 
    [ 2 ] - Multiplicar           
    [ 3 ] - Maior                 
    [ 4 ] - Novos Números         
    [ 5 ] - Sair do Programa      
    ------------------------------''')
    opcao = int(input(': '))

    if opcao == 1:
        print(f'{numero1} + {numero2} = {numero1 + numero2}')
    elif opcao == 2:
        print(f'{numero1} x {numero2} = {numero1 * numero2}')
    elif opcao == 3:
        if numero1 > numero2:
            print(f'O 1º número é o maior({numero1})')
        elif numero2 > numero1:
            print(f'O 2º número é o maior({numero2})')
        else:
            print('O números são iguais')
    elif opcao == 4:
        numero1 = int(input('Digite o 1º Número: '))
        numero2 = int(input('Digite o 2º Número: '))
    elif opcao == 5:
        print('Termino do Programa')