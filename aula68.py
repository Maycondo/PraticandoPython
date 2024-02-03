




def ParorImpar(numero):

    Parouimpar = numero % 2 == 0

    if Parouimpar:
        return f'{Parouimpar} esse numero é par'
    else:
        return  f'{Parouimpar} esse número é impar'
  


print(ParorImpar(345))

