num1 = float(input('Digite o 1º Num: '))
num2 = float(input('Digite o 2º Num: '))

if num1 > num2:
    print(f'O primeiro valor é maior! ({num1})')
elif num2 > num1:
    print(f'O segundo valor é maior! ({num2})')
else:
    print(f'Não existe valor maior, os dois são iguais! ({num1})')
