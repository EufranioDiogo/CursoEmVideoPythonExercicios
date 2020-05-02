numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'dozese', 'treze', 'quatorze', 'quinze', 'dezasseis', 'dezassete', 'dezoito', 'dezanove', 'vinte')

numero = int(input('Digite um número entre(0 e 20): '))

while numero < 0 or numero > 20:
    numero = int(input('Digite novamente um número entre(0 e 20): '))

print(f'{numero} = {numeros[numero]}')
