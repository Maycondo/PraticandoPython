


class carro:
    def  __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
       print(f'{self.marca} {self.modelo} está acelrando...')




Car1 = carro("Fiat", "Ducato")
Car1.acelerar()

Car2 = carro("Chevrolet", "Corsa")
Car2.acelerar()