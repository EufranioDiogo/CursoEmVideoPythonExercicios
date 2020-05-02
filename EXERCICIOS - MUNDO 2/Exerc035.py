nome = ''
preco = 0.0
total = 0
produtoAcima1000 = 0
nomeProdutoMaisBarato = ''
menorPreco = 0
flag = 0

while True:
    nome = input('Digite o nome do produto: ').strip().title()
    preco = float(input('Preço produto: '))
    while preco < 0.0:
        preco = float(input('Digite novamente o preço do Produto: '))
    if preco > 1000.0:
        produtoAcima1000 += 1
    if flag == 0:
        nomeProdutoMaisBarato = nome
        menorPreco = preco
        flag = 1
    else:
        if preco < menorPreco:
            menorPreco = preco
            nomeProdutoMaisBarato = nome

    total += preco
    opcao = input('Deseja continuar?(s/n) ').strip().lower()[0]
    if opcao == 'n':
        break

print(f'''
----------------------------------------
Total: {total:.2f} AOA
Quant. Prod. Mais que 1000 AOA: {produtoAcima1000}
Nome Produto Mais Barato: {nomeProdutoMaisBarato}''')