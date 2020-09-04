from time import sleep
print('~'*30)
print(f'\033[1:33mTABUADA V3.0\033[m')
print('~'*30)

while True:
    n = int(input('Digite um número para a tabuada (Negativo para sair): '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
    print('-'*30)
    sleep(1.5)
