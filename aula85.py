

# Programaçao orienta a objetos com classe é construtor


hora = int(float(input('Digite á hora de hoje')))

hora_hoje = hora

if hora_hoje >= 0 and hora_hoje < 12:
    print('Bom dia! Agora são',hora_hoje,'horas.')
elif  hora_hoje == 12 or (hora_hoje >= 13 and hora_hoje <= 18):
    print('Boa tarde! Agora são',hora_hoje,'horas.')
if hora_hoje > 18 or hora_hoje < 4:
    print('Boa noite! Agora são',hora_hoje,'horas.')