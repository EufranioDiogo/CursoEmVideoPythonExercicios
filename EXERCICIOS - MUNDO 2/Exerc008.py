print('Cálculo IMC')
altura = float(input('Digite a sua altura: '))
peso = float(input('Digite o seu peso: '))

if (0 < peso < 300) and (0 < altura < 3.5):
    imc = peso / altura ** 2

    if imc < 18.5:
        print('Você está abaixo do peso!')
    elif imc < 25:
        print('Você tem um peso normal!')
    elif imc < 30:
        print('Você está em Sobrepeso')
    elif imc < 35:
        print('Você está em Obesidade grau 1')
    elif imc < 40:
        print('Você está em Obesidade grau 2')
    else:
        print('Você está em Obesidade grau 3')
else:
    print(f'Dados incertos')
