from time import sleep
print('-='*18)
print(f'\033[1:33mCAIXA ELETRÔNICO SIMPLES\033[m')
print('-='*18)

saque = int(input('Informe o valor desejado: R$'))

total = saque
ced = 50
totalced = 0
sleep(0.5)
print('\033[1:35mCALCULANDO ... \033[m')
sleep(2)
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'{totalced} nota(as) de R${ced},00.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
