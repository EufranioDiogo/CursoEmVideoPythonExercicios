palavras = ('youtube', 'eufranio', 'computador', 'python', 'java', 'louco', 'diamante', 'ltf')
vogaisEncontradas = ''
flag = False


for palavra in palavras:
    for vogal in palavra:
        if vogal in 'aeiou':
            vogaisEncontradas += vogal + ', '
            flag = True
    if flag:
        print(f'A palavra {palavra} tem as seguintes vogais: {vogaisEncontradas}')
        flag = False
    else:
        print(f'A palavra {palavra} não tem vogais')
    vogaisEncontradas = ''
