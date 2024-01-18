"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

#Numero_digitador = input('Digite um numero:')

#if  Numero_digitador.isdigit():
#   Numero_digitador_init = int(Numero_digitador)
#    par_impar = Numero_digitador_init % 2 == 0
#    par_impar_Texto = 'Impar'


#    if par_impar:
#       par_impar_Texto = 'par'


#   print(f"0 numero {Numero_digitador_init} é {par_impar_Texto}")
#else:
#    print('Voce não digito nenhum numero')


"""
Faça um programa que exige a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação correspondente. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

#entrada = input("Digite o horário em numeros em inteiros")

#try:
#    Horas = int(entrada)


#    if Horas >= 0 and Horas <= 11:
#         print('Bom dia!')
#    elif Horas >= 12 and Horas <= 17:
#         print('Bom tarde')
#    elif Horas >= 18 and Horas <= 23:
#        print('Boa noite')
#    else:
#         print('Não conheço esse numero.')
#except:
#      print('Cara! só pode digita numeros.')

"""
Faça um programa que parte do primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
“Seu nome é normal”; maior que 6 escreva "Seu nome é muito grande".
"""

Name = input('Digite o seu nome')
Tamanho_Name = len(Name)

if Tamanho_Name > 1:
    if Tamanho_Name <= 4 :
      print ('Seu nome é curto')

      
    elif Tamanho_Name >= 5 and Tamanho_Name <=6:
       print ('Seu nome é normal')
    else: 
       print('Seu nome é grande')
else:
    print('Ai! coloque o seu nome na moralzinha')