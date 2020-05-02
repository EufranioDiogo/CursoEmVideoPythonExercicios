l1 = float(input('1º Segmento: '))
l2 = float(input('2º Segmento: '))
l3 = float(input('3º Segmento: '))

if l1 + l2 > l3 and l2 + l3 > l1 and l3 + l1 > l2:
    print(f'Pode formar um triângulo')
else:
    print('Os segmentos acima não podem formar triângulo')
