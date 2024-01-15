





Numero_str = input('Digite um numero')

try:
    print('STR:', Numero_str)
    Numero_float = float(Numero_str)
    print('FLOAT', Numero_float)
    print(f'O dobro de {Numero_str} é {Numero_float * 2}')
except:
    print('Isso nao é um numero')


#if Numero_str.isdigit():
#    Numero_Flot = float(Numero_str)
#    print(f'O tripo de {Numero_str} é {Numero_Flot * 3:.0f}')
#else:
#    print('Isso não é um número')
