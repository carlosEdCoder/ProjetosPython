print(f'\033[1:33mMAIS VELHO DO GRUPO\033[m')

somatorio = 0
idadeVelho = 0
nomeVelho = ''
mulherCont = 0

for c in range(1, 5):
    nome = str(input(f'Informe o nome da {c}° pessoa: ')).title().strip()
    idade = int(input(f'Informe a idade da {c}° pessoa:'))
    sexo = str(input(f'Informe o sexo da {c}° pessoa (M ou F): ')).upper().strip()
    print(f'{"-=" *20}')
    somatorio += idade

    if idade > idadeVelho and sexo == 'M':
        nomeVelho = nome
        idadeVelho = idade

    if idade < 20 and sexo == 'F':
        mulherCont += 1

print(f'''A média de idade do grupo é de {somatorio / 4} anos;
{nomeVelho} é o homem mais velho do grupo e tem {idadeVelho} anos;
{mulherCont} mulher(es) tem menos de 20 anos.''')
