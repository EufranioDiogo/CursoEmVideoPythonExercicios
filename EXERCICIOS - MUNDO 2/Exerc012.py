i = 0
print('[', end='')

for i in range(1, 50):
    if i % 2 == 0:
        print(i, end=', ')

if (i+1) % 2 == 0:
    print(i+1, end=']')
