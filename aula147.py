

class Meta(type):
    def __new__(mcs, name, bases, dct):
        print('METACLASS NEW')
        cls = super().__new__(cls)
        return cls
    

class Perso(metaclass=Meta):    
    def __new__(cls, *args, **kwargs):
        print('MEU NEW')
        instancia = super().__new__(cls)
        return instancia
    
    def __init__(self, name):
        print('MEU INIT')
        self.name = name 
