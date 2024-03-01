# Funções decoradas e decoradas
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradas são funções que decoram outras funções
# Decoradores são usados ​​para fazer o Python
# usar as funções decoradas em outras funções.

def  criar_funcao(func):
    def interna(*args, **kwargs):
        for arg in args:
            e_sttring(arg)
        resultado = func(*args, **kwargs)
        
        return resultado
    return interna


@criar_funcao   
def inverte_string(string):
    return string[::-1]


def e_sttring(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')



invertida = inverte_string('Michael')
print(invertida)