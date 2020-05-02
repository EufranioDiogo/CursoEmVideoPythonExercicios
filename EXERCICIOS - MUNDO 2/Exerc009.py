precoNormal = float(input('Digite o preço do produto: '))
desconto = 0
juros = 0

if precoNormal > 0:
    condPagamento = input('''Condição de pagamento:
    Dinheiro/Cheque - 1
    Cartão - 2
    2x no Cartão - 3
    3x ou mais - 4
    : ''')[0]

    if condPagamento == '1':
        desconto = precoNormal % 0.1
        print(f'O produto será vendido a {precoNormal - desconto} AOA\nDesconto(10%): {desconto} AOA')
    elif condPagamento == '2':
        desconto = precoNormal % 0.05
        print(f'O produto será vendido a {precoNormal - desconto} AOA\nDesconto(5%): {desconto} AOA')
    elif condPagamento == '3':
        desconto = 0
        print(f'O produto será vendido ao preço normal sem Desconto(0%): {precoNormal} AOA')
    elif condPagamento == '4':
        juros = precoNormal % 0.2
        print(f'O produto será vendido com juros(20%) de {juros} AOA\nPreço Produto + Juros: {precoNormal + juros} AOA')
    else:
        print('Cond. Pagamento Inválida!')