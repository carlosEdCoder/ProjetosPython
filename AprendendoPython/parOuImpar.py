from time import sleep
from random import randint
print('-='*13)
print(f'\033[1:33mJOGO PAR OU ÍMPAR\033[m')
print('-='*13)

player = cpu = 0
while True:
    sleep(1.5)
    print('-'*25)
    print(f'\033[1:35mPlayer {player} X CPU {cpu}\033[m')
    print(f'''[1] Ímpar\n[2] Par\n[0]SAIR''')
    opcao = int(input('Digite sua escolha: '))
    print('-'*25)

    while opcao > 2 or opcao < 0:
        print(f'Opção Inválida!! Tente Novamente.')
        print(f'''[1] Ímpar\n[2] Par\n[0]SAIR''')
        opcao = int(input('Digite sua escolha: '))
        print('-' * 25)

    if opcao == 0:
        break

    pc = randint(1, 10)
    n = int(input('Digite um número: '))
    print(f'O CPU jogou {pc}. Você jogou {n}.')

    if opcao == 1:
        if (n + pc) % 2 == 1:
            print(f'Você ganhou! {n + pc} é ímpar.')
            player += 1
        else:
            print(f'Você perdeu! {n + pc} é par.')
            cpu += 1
    elif opcao == 2:
        if (n + pc) % 2 == 0:
            print(f'Você ganhou! {n + pc} é par.')
            player += 1
        else:
            print(f'Você perdeu! {n + pc} é ímpar.')
            cpu += 1
