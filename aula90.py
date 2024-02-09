

class animal:
    def __init__(self, name):
        self.name = name

    
    def comendo(self, alimento):
        return f"{self.name} está comendo {alimento}"
    
    def executar(self, *args, **kwargs): 
        return self.comendo(*args, * kwargs)






Animal1 = animal(name='lion')

print(Animal1.name)
print(Animal1.executar("Carne"))



