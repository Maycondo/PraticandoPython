
import _json

CAMINHO_ARQUIVO = "aula127.json"


class Perso:
    def __init__(self, name, age):
        self.name = name
        self.age = age




p1 = Perso('Maria', 20)
p2 = Perso('Beatriz', 23)
p3 = Perso('João', 45)

with open(CAMINHO_ARQUIVO, 'w') as aquivo:
    ...
 #   _json.dump(bd, arquivo, ensure_ascrii=False, indent=2)

