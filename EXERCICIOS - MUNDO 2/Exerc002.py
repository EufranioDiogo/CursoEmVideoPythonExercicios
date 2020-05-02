result = 0
numero = int(input('Digite um número: '))
base = input('''
Qual base de conversão pertende:
1 - Binária
2 - Hexadecimal
3 - Octal
: ''').strip().lower()[0]

if base == '1':
    result = bin(numero)[2:]
    print(f'{numero}(BASE 10) = {result}(BASE 2)')
elif base == '2':
    result = hex(numero).upper()[2:]
    print(f'{numero}(BASE 10) = {result}(BASE 16)')
elif base == '3':
    result = oct(numero)[2:]
    print(f'{numero}(BASE 10) = {result}(BASE 8)')
else:
    print('Opção inválida')