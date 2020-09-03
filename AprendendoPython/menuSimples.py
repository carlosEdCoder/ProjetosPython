from time import sleep
print(f'\033[1:33mMENU DE OPÇÕES SIMPLES\033[m')

controle = 0
n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))

while controle != 5:
    controle = int(input(f'''[1]Somar
[2]Multiplicar
[3]Maior Valor
[4]Novos Números
[5]SAIR
Escolha sua opção: '''))
    sleep(1.5)
    if controle == 1:
        print(f'''{"=-"*20}\n{n1} + {n2} = {n1 + n2}\n{"=-"*20}''')
        sleep(1.5)

    elif controle == 2:
       print(f'''{"=-"*20}\n{n1} x {n2} = {n1 * n2}\n{"=-"*20}''')
       sleep(1.5)

    elif controle == 3:
       if n1 > n2:
           print(f'''{"=-"*20}\n{n1} é maior do que {n2}.\n{"=-"*20}''')
           sleep(1.5)
       elif n1 == n2:
           print(f'''{"=-"*20}\n{n1} é igual {n2}.\n{"=-"*20}''')
           sleep(1.5)
       else:
           print(f'''{"=-"*20}\n{n2} é maior do que {n1}.\n{"=-"*20}''')
           sleep(1.5)

    elif controle == 4:
        n1 = int(input(f'Digite o primeiro número: '))
        n2 = int(input(f'Digite o segundo número: '))
        print(f'{"=-"*20}')
        sleep(1.5)

    elif controle > 5 or controle < 1:
        print(f'''{"=-"*20}\nOpção inválida! Tente Novamente.\n{"=-"*20}''')
        sleep(1.5)
        