import json 

from aula92_A import CAMINHO_ARQUIVO, Perso

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    pessoas = json.load(arquivo)
    p1 = Perso(**pessoas[0])
    p2 = Perso(**pessoas[1])




