
name = input('Digite o seu nome')
age = input('Digite a sua idade')

if name and age:
    print(f'Seu nome é {name}')
    print(f'Seu nome invertido é {name[::-1]}')


    if ' ' in name:
        print('Seu nome contem espaços')
    else:
        print('Seu nome não contem espaços')
    

    print(f'Seu nome tem {len(name)} letras')
    print(f'A primeira letra do seu nome é {name[0]}')
    print(f'A ultimo letra do seu nome é {name[-1]}')
else:
    print('Desculpe, voce deixou campos vazios.')