from time import sleep
print('-='*17)
print(f'\033[1:33mREGISTRO DE PRODUTOS\033[m')
print('-='*17)

totalG = maisMil = pMaisB = 0
nMaisB = ''

while True:

    print('-'*34)
    nomeProduto = str(input(f'Produto: ')).strip().upper()
    preco = float(input('Preço: R$'))

    if pMaisB == 0:
        pMaisB = preco
        nMaisB = nomeProduto
    elif preco < pMaisB:
        pMaisB = preco
        nMaisB = nomeProduto

    if preco > 1000:
        maisMil += 1

    totalG += preco

    op = str(input('Mais algum produto (S/N)? ')).strip().lower()[0]

    while op not in 'sSnN':
        op = str(input('Mais algum produto (S/N)? ')).strip().lower()[0]

    if op in 'nN':
        break

print('-'*34)
print('\033[1:35mFINALIZANDO SUA COMPRA ...\033[m')
sleep(2)
print('-'*34)
print(f'\033[1:35mCOMPRA FINALIZADA\033[m')
print(f'''Você gastou um total de R${totalG:.2f};
{maisMil} produtos custaram mais de R$1000,00;
{nMaisB} foi o produto mais barato que você comprou, e custou R${pMaisB:.2f}.''')
