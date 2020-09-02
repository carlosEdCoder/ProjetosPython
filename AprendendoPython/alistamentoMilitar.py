from datetime import date
print(f'\033[1:33mALISTAMENTO SIMPLES\033[m')
anoAtual = date.today().year
nascimento = int(input('Informe o seu ano de nascimento: '))
idade = anoAtual - nascimento

if idade < 18:
    print(f'''Quem nasceu em {nascimento} faz {idade} anos em {anoAtual}.
Falta aproximadamente {18 - idade} anos para você se alistar.
Alistamento previsto para {(18 - idade) + anoAtual}.''')
elif idade == 18:
    print(f'''Quem nasceu em {nascimento} faz {idade} anos em {anoAtual}.
Você deve se alistar imediatamente, caso ainda não tenha feito.''')
else:
    print(f'''Quem nasceu em {nascimento} faz {idade} anos em {anoAtual}.
Você já passou do tempo de se alistar.''')