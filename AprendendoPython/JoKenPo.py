import random
from time import sleep
print(f'\033[1:33mJO KEN PO\033[m')
opcoes = ['Pedra', 'Papel', 'Tesoura']
computador = random.randint(0, 2)
print(f'''Opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Selecione sua jogada: '))

sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)

print(f'''{'--*--'*3}
O computador escolheu {opcoes[computador]}
Você escolheu {opcoes[jogador]}
{'--*--'*3}''')

if computador == 0:  # pedra
    if jogador == 0:
        print('===EMPATE===')
    elif jogador == 1:
        print('===VOCÊ GANHOU===')
    elif jogador == 2:
        print('===VOCÊ PERDEU===')

elif computador == 1:  # papel
    if jogador == 0:
        print('===VOCÊ PERDEU===')
    elif jogador == 1:
        print('===EMPATE===')
    elif jogador == 2:
        print('===VOCÊ GANHOU===')

elif computador == 2:  # tesoura
    if jogador == 0:
        print('===VOCÊ GANHOU===')
    elif jogador == 1:
        print('===VOCÊ PERDEU===')
    elif jogador == 2:
        print('===EMPATE===')
