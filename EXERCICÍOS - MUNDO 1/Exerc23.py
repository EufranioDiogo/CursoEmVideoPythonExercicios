data = int(input('Digite um número de 0 a 9999: '))
milhares = data//1000
centena = (data % 1000)//100
dezena = ((data % 1000) % 100)//10
unidade = data % 10
print('|Unidade: ', unidade, '|Dezena: ', dezena, '|Centena: ', centena, '|Milhar: ', milhares)
