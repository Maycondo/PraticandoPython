'''''


def fora():
    a = 1
    def dentro():

        print(dentro.__code__.co)
        return a
    return dentro


dentro1 = fora(10)
dentro2 = fora(20)

print(dentro1())
print(dentro2())
'''''
def concatenar(string_inicial):
    valor_final = string_inicial

    def interga(valor_a_concatenar):
        nonlocal valor_final

        valor_final += valor_a_concatenar
        return valor_final
    return interga



c = concatenar('a')

print(c('b'))
print(c('c'))
print(c('d'))
final = c()

print(final)




