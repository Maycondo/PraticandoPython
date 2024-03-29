import contas

class Perso:
    def  __init__(self, name: str, age: int) -> None: 
        self.name = name
        self.age = age
    

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name: str):
        self._name = name
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self , age: int):
        self._age = age

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.age!r}, {self._age!r})'
        return f'{class_name} {attrs}'
        

class Cliente(Perso):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.conta: contas 
