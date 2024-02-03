


perso = {

    'name':  "Michel",
    'surname': "Douglas",
    'age':  30,
    'city': "Rio largo",
    'endereço': [
        {'rua':'Rua quinze vila rica','número':7,'bairro':'Mata do rolo',}
        ],
}


print(dict(name="Michael", surname="Douglas", age=30))
print(perso['name'])

for chaves in perso:    
    print(chaves, perso[chaves])