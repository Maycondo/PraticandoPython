""" Calculadora com white"""

while True:

    numero = input("Digite um número: ")
    numero2 = input("Digite outro número: ")
    operador = input("Digite um operador +-/*: ")

    numeros_validos = True
    float_numero1 = 0
    float_numero2 = 0

    try: 
       
       float_numero1 = float(numero)
       float_numero2 = float(numero2)
       numeros_validos = True
    except:
        numeros_validos = None

        if numeros_validos is None:
         print("Um ou ambos dos numéros digitados são inválidos")
         continue
        
        if len(operador) > 1:
         print('Digite apenas uma operador.')
         continue

        Operadores_permitidos = "+-/*"

        if operador not in Operadores_permitidos:
         print("O operador informado é inválido. Por favor, digite só desses operadores +,-, /, *")
         continue

        if operador == '+':
          print(f"{float_numero1}+{float_numero2}=", float_numero1 + float_numero2)
        elif operador == "-":
          print(f"{float_numero1}-{float_numero2}=", float_numero1 - float_numero2)
        elif operador == "/":
          print(f"{float_numero1}/{float_numero2}=", float_numero1 / float_numero2)
        elif operador == "*":
          print(f"{float_numero1}*{float_numero2}=", float_numero1 * float_numero2)
        else:
          print("Nunca deveria chegar aqui.")

###
        sair = input('Quer sair? [s]im: ').lower().startswith()

    if sair is True:
       break



