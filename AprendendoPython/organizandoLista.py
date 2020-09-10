print('-='*18)
print(f'\033[1:33mORGANIZANDO LISTA\033[m')
print('-='*18)

lista = list()
for c in range(0, 5):
    n = int(input(f'Digite o {c+1}° número: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print(f'Número adicionado no final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Número adicionado na posição {pos+1}.')
                break
            pos += 1
print(f'Resultado da lista > {lista}')
