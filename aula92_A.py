# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import  json


CAMINHO_ARQUIVO = "aula127.json"


class Perso:
    def  __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Perso(nome="João", idade=25)
p2 = Perso(nome="Maria", idade=30)
p3 = Perso(nome="Pedro", idade=45)
bd = [p1, p2, p3]


with open(CAMINHO_ARQUIVO, "w") as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)
