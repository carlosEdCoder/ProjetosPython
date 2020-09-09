print('-='*18)
print(f'\033[1:33mAÇOUGUE\033[m')
print('-='*18)

tupla = ('acem', 23.80, 'cha de fora', 25.80, 'patinho', 26.80, 'cha de dentro', 27.80, 'alcatra', 29.80)

for c in range(0, 9, 2):
    print(f'{tupla[c]:.<20}{tupla[c + 1]:.>10.2f}')
