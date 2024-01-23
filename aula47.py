"""""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""


palavra_secreta = "Espaço tempo"
letra_acertadas = ""
numeros_tentativas = 0

#import os

while True:

    letra_Digitada = input("Digite uma letra: ")
    numeros_tentativas += 1

    if len(letra_Digitada) > 1:
        print("Digite apenas uma letra ")
        continue

    if letra_Digitada in palavra_secreta:
        letra_acertadas += letra_Digitada

    palavra_forma = ""
    for letra_secreta in palavra_secreta:
      if letra_secreta in letra_secreta:
           palavra_forma += letra_secreta
      else:
          palavra_forma += "*"

    print(palavra_forma)

    if palavra_forma == palavra_secreta:
         # os.system("clear")
          print("VOCÊ GANHOU! PARABÉNS!")
          print("A palavra era ", palavra_secreta)
          print("Tentativas", numeros_tentativas)
          letra_acertadas = ""
          numeros_tentativas = 0


