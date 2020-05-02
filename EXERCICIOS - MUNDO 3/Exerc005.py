nomes = ('Lápis', 'Borracha', 'Caderno', 'Estojo', 'Transferidor', 'Compasso', 'Mochila', 'Canetas', 'Livro')
preço = (1.75, 2.00, 15.90, 25.00, 4.20, 9.99, 120.32, 22.30, 34.90)
titulo = 'Listagem de Preços'

print('-'*50)
print(f'{titulo.upper():^50}')
print('-'*50)

for i in range(0, len(nomes)):
    print(f'{nomes[i]:.<35}AOA {preço[i]:>10.2f}')
print('-'*50)
