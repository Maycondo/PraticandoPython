# atributos de class 


class Perso:

    ano_atual = 2024


    def __init__(self, name, surname, age):
        self.name = name 
        self.surname = surname 
        self.age = age

    def data_nascimento(self):
        return Perso.ano_atual - self.age
    


p1 = Perso('Michel', 'douglas', 21)

print(f'A usuario {p1.name} {p1.surname} com idade de {p1.age} anos! Nascimento em {p1.data_nascimento()}')