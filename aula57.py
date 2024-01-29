

import os


#Essa lista será usada para armazenar os elementos inseridos pelo usuário.

lista = []


#Inicia um loop infinito.

while True:

    #Imprime uma mensagem para o usuário, pedindo que ele selecione uma opção.
    print('Selecione um opção')

    #Solicita uma entrada do usuário. O usuário deve inserir 'i', 'a' ou 'l' 
    #para escolher entre inserir, apagar ou listar elementos.

    opçao = input('[i]nserir [a]pagar [l]ista: ')


    if opçao == 'i':
        os.system('clear')
        valor = input('Valor: ')
        lista.append(valor)
    elif opçao == 'a':
        indice_str = input(
            'Escolha o indice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except:
            print('Não foi possivel apagar esse indice')

    elif opçao == "l":
        os.system("clear")
           
        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)