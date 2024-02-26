

class Perso:
    def  __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.falando = False


    
    def falar(self, falando):
        self.falando = falando

        if  self.falando == True:
            print(f'{self.name} {self.surname} está falando')
        if self.falando == False:
            print(f"{self.name} {self.surname} parou de falar")




p1 =  Perso("John", "Doe")
p1.falar(True)
