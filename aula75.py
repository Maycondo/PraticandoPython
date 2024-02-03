



perguntas = [

    {
        'Pergunta': 'Quando é 2+2?',
        'opções': ['1', '2', '4', '5'],
        'resposta correta': '4',
    },

    {
        'Pergunta': 'Quando é 5*5',
        'opções': ['20', '30', '60', '70'],
        'resposta correta': '25',
    },

    {
        'Pergunta': 'Quando é 10/2',
        'opções': ['4', '5', '2', '1'], 
        'Resposta': '5',

    },
]


for pergunta in perguntas:
    print('Pergunta:',pergunta['Pergunta'])


    for i, opções in enumerate('opções'):
       print(f'{i})', opções)


    escolha = input('Escolha uma opção: ')

    acerto =  False
    escolha_init = None
    qnd_opcoes = len(opções)


    if escolha.isdigit():
      escolha_init = int(escolha)

    if escolha is not None:
       if  escolha_init >= 0 and escolha_init < qnd_opcoes:
          if opções[escolha_init] == pergunta['Resposta']:
             acerto = True
    

    if acerto:
       print('Parabéns! Você acertou')
    else:
       print('Você errou, a resposta era ', pergunta['Resposta'])

       break
