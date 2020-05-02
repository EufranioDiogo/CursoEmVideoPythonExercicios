from datetime import date
desc = 'alistamento Militar'.title()
print('#.#'*10)
print(f'{desc:-^15}')
print('#.#'*10)

anoNascimento = int(input('Digite o seu ano de nascimento: '))
sexo = input('Digite o seu sexo(Masculino - M/ Femenino - F): ').strip().lower()[0]

if sexo == 'm':
    if anoNascimento > 1900:
        idade = date.today().year - anoNascimento
        if idade > 18:
            print(f'Já devia ter feito o alistamento militar, acerca de {idade - 18} ano(s)')
        elif idade < 18:
            print(f'Ainda não pode fazer o alistamento militar, somente daqui a {18 - idade} ano(s)')
        else:
            print(f'Está na hora deve fazer o alistamento militar!')
    else:
        print('Ano Inválido')
elif sexo == 'f':
    print('Não é necessário fazer o alistamento militar por ser menina')
else:
    print('Sexo desconhecido!')