

ano = int(input('Digite o ano atual:  '))


if ano %4 == 0 and ano%100 != 0  or ano %400 == 0:
    print('Ano bissexto')
else:
    print('Ano nao e bissexto')