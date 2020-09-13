print('-='*18)
print(f'\033[1:33mEXERCICIO 87\033[m')
print('-='*18)

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = coluna3 = maior2 = 0

# Construindo a Matriz

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para a posição {[l]}{[c]}: '))

print('-='*18)

# Matriz completa

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()

print('-='*18)

# Somatório dos números pares;

for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]

print(f'O somatórtio de todos os números pares digitados resulta em {pares}.')

#Somatório de todos os números da terceira coluna;

for l in range(0, 3):
    coluna3 += matriz[l][2]

print(f'Somatório dos valores da coluna 3: {coluna3}')

# Maior valor da segunda coluna;

for l in range(0, 3):
    if l == 0:
        maior2 = matriz[l][1]
    elif matriz[l][1] > maior2:
        maior2 = matriz[l][1]

print(f'Maior valor da segunda coluna é {maior2}')
