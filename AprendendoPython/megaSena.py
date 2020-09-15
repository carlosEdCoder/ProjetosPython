from random import randint
from time import sleep

print('-='*18)
print(f'\033[1:33mEXERCÍCIO\033[m')
print('-='*18)

jogo = list()
temp = list()

print('-='*5 ,f'   MEGA SENA   ', '-='*5)

palpite = int(input('Quantos palpites você deseja? '))

print('-='*5, f'  COMPUTANDO   ', '-='*5)

# Um ciclo 'for' para controlar a quantidade de palpites gerados;
for c in range(0, palpite):
    cont = 0

    # Um ciclo 'while' que gera palpites com 6 números distintos randômicos ordenados e os insere na lista 'jogo'
    while True:
        n = randint(1, 60)
        if n not in temp:
            temp.append(n)
            cont += 1

        if cont >= 6:
            temp.sort()
            jogo.append(temp[:])
            temp.clear()
            break

# Print de cada jogo inserido na lista 'jogo';
sleep(1)
for p, j in enumerate(jogo):
    print(f'Palpite {p + 1}: {j}')
    sleep(1)

print('-='*5 ,f'   BOA SORTE   ', '-='*5)
