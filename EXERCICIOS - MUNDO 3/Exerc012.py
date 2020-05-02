expressao = input('Digite a expressão: ')
abertura = 0
fechamento = 0


for i in range(0, len(expressao)):
    if expressao[i] == '(':
        abertura += 1
    elif expressao == ')':
        fechamento += 1
if abertura == fechamento:
    print(f'A expressão: {expressao} é VALIDA')
else:
    print(f'A expressão: {expressao} é NÃO VALIDA')
