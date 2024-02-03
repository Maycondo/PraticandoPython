

    

def Criar_multiplicador(multripicador):
    def multripica(numero):
        return numero * multripicador
    return multripica

duplicar = Criar_multiplicador(2)
triplificar = Criar_multiplicador(3)
quadruplicar = Criar_multiplicador(4)

print(quadruplicar(6))