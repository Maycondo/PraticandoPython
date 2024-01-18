"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)

"""
velocidade = 67  # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

Car_maior_radar = velocidade > RADAR_1
Car_mutador_1 = local_carro >= (LOCAL_1 - RADAR_RANGE)
Car_mutador_2 = local_carro <= (LOCAL_1 + RADAR_RANGE)


if  Car_maior_radar:
    print(f'Velocidade excessiva! Mantenha-se abaixo')

if Car_mutador_1 and Car_mutador_2 and Car_maior_radar:
    print('Carro multado em radar 1')