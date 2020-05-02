valorCasa = float(input('Digite o valor da casa: '))
salarioCliente = float(input('Digite o valor do Salário do Cliente: '))
quantAnosPagar = int(input('Em quantos anos pretende pagar: '))

valorPrestacao = valorCasa / (quantAnosPagar * 12)

if salarioCliente > 0 and valorCasa > 0 and quantAnosPagar > 0:
    if valorPrestacao > salarioCliente * 0.3:
        print(f'Emprestimo não concedido, porque o valor de prestação mensal da casa é de: {valorPrestacao} AOA, superior a 30% do seu salário')
    else:
        print(f'Emprestimo concedido\nValor Prestação Mensal: {valorPrestacao} AOA\nQuant Meses: {quantAnosPagar*12}\nSalário Restante: {salarioCliente-valorPrestacao} AOA')
