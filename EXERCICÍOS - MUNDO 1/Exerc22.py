nome = input('Digite o seu nome por-favor: ')
quantLetras = len(''.join(nome.strip().split()))
print(f'''Nome letras maiusculas: {nome.strip().upper()}
Nome letras minusculas: {nome.strip().lower()}
Quant Letras: {quantLetras}
Quant Letras Primeiro nome: {len(nome.strip().split()[0])}''')
