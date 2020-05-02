frase = input('Digite uma frase: ').strip().upper()
j = len(frase) - 1
flag = 0

for i in range(0, len(frase)):
    if frase[i] != frase[j]:
        flag = 1
        break
    j -= 1

if flag == 0:
    print(f'A frase:\n{frase}\nÉ a Palindrome')
else:
    print(f'A frase:\n{frase}\nNão é a Palindrome')