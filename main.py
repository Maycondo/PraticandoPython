
"""""

name = input("Michel")
suarname = input("Douglas")
age = int(input(20))

print(name)
print(suarname)
print(type(age))

"""

""""

soma = 1+1
multiplicaçao = 2 * 2
divisao = 30 / 3
potencia = 7**2

print("soma", soma)
print("multiplicaçao", multiplicaçao)
print("divisao", divisao)

"""

"""""

idade = int( input("Informe sua idade:") ) 

if idade >= 18:
    print("Permetido!")
else:
    print("Bloqueado!")

"""

"""""

Salario = float( input("Informe o salário:  "))

if Salario <= 3000:
    print(" Programador Junior")
elif Salario > 3000 and Salario <= 6000:
    print(" Programador pleno")
elif Salario > 6000 and Salario <= 15000:
    print(" Programador Senior")
else:
     print(" Gerente de projetos")

     
"""

""""

Lista_numeros = [1, 2 ,3 ]

Lista_numeros[0] = 5

print(Lista_numeros[0])

"""

'''''

Notas = []

for x in range(300):
    Codigo_aluno = input("RM: ")
    nota = float(input("Nota: "))
    resultado = [Codigo_aluno, nota]
    Notas.append(resultado)  

    print( "Quantidade de notas", len(Notas) ) 

    for n in Notas: 
        Codigo_aluno = n[0]
        nota = n[1]
        print("O RM", Codigo_aluno, "Tirou a nota:", nota)

'''

'''''
notas = []

contador = 1

while contador <= 5:
    Codigo_aluno = input("RM: ")
    nota = float(input("Nota: "))
    resultado = [Codigo_aluno, nota]
    notas.append(resultado)

    contador = contador + 1

print( "Quantdade de notas", len(notas))

'''

''''
perso = {
    "name": "Programa Python",
    "idade": 27,
    "peso": 70.2,
}

print( perso['name'])
print( perso["idade"])
print( perso["peso"])

'''

""""

import os

messagens = []

name = input("Nome: ")

"""

''''
Funçoes


'''

def minha_funçao(valor1, valor2):
    return valor1 + valor2

resposta = minha_funçao(10, 10)

print("Resposta", resposta)