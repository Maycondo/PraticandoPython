

#iterando strings com white

name = 'Maycon douglas' #iteraveis

tamanho_name = len(name)

print(name)
print(name[5])
print(tamanho_name)



index = 0
while index < len(name):
    letra = name[index]
    novo_name = letra
    index += 1
    
print(novo_name)