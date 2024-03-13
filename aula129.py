

"""""

class Perso:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


p1 = Perso('Michael', 'douglas')

print(f'{p1.name} {p1.surname}')



class Carro:
    def __init__(self, marca, cor, motor):
        self.marca = marca
        self.cor = cor
        self.motor = motor

    def Acelerando(self):
        Acelerando = 'Acelerou!'
        return Acelerando
    

Car1 = Carro('fiat', 'vermelho', 'V8')

print(f'O carro da marca {Car1.marca} de cor {Car1.cor} {Car1.Acelerando()}.')


class animal:
    def  __init__(self, nome, especie):
       self.nome = nome 
       self.especie = especie

    def abateu(self):
        print(f'{self.nome} da especie {self.especie} abateu uma zebra...')
    



Leon = animal( "Lion", "Panthera leo")
Leon.abateu()

"""

class camera:
    def __init__(self, name, filmando=True):
        self.name = name 
        self.filmando = filmando    
    
    def filmar(self):
        if self.filmando:
           print(f'{self.name} Ja esta filmando...')
           return 
         
        print(f'{self.name} esta filmando')
        self.filmando = True

    def para_filmar(self):
        if not self.filmando:
            print(f'{self.name} Nao esta filmando.')
            return
        
        print(f'{self.name} esta parando fotografando...')
        self.filmando = False

    def fotografar(self):
        if self.filmando:
            print(f'{self.name} nao pode fotografar filmando.')
            return
        
        print(f'{self.name} esta fotografando...')




c1 = camera("Sony")
c2 = camera("Canon")