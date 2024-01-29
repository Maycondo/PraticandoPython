"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7


"""


# Esse codigo calcula os dois digito verificando de um numero de CPF nove digitos.

Cpd_eviando_uruario = '84955162096'
    
# Isso pega os primeiros nove digitos do CPF e amarzena em variavel 

Nove_digitos = Cpd_eviando_uruario[:9]

# Calculando primeiro digito verificador
# Essa parte do codigo multlipicando cada digito pelo valores de uma contagem regressiva de 10 a 2
contagem_regressivo_1 = 10
resultado = 0
for digito_1 in Nove_digitos:
    resultado += int(digito_1) * contagem_regressivo_1
    contagem_regressivo_1 -= 1

digito_1 = resultado * 10 % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

# Agora contém os primeiros 10 digitos do CPF (nove digitos originais + primeiro digito verificador)
dez_digitos = Nove_digitos + str(digito_1)

# Calculo do segundo digito verificador
# Siliar ao codigo superio esse trecho mulplica cada digito pelos valores de uma contagem regressiva de 11 a 2
contagem_regressivo_2 = 11
resultado_digito_2 = 0

for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contagem_regressivo_2
    contagem_regressivo_2 -= 1

digito_2 = resultado_digito_2 * 10 % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

# imprimindo o segundo digito verificador
print(digito_2)




