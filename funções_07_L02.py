#Embaralha palavra. Construa uma função que
#  receba uma string como parâmetro e devolva outra string
#  com os carateres embaralhados.
#  Por exemplo: se função receber a palavra python,
#  pode retornar npthyo, ophtyn ou qualquer outra combinação possível,
#  de forma aleatória. Padronize em sua função que todos
#  os caracteres serão devolvidos em caixa alta ou caixa baixa, 
# independentemente de como foram digitados.


#random.shuffle(lista) === embaralha os elementos de uma lista
import random
# a = input('Digite uma palavra: ').lower()
# def ran(a):
#     b = ''
#     a = list(a)
#     random.shuffle(a)
#     for i in a:
#         b += i
#     return(b)

# print('A palavra embaralhada é: %s' % (ran(a)))

def embaralha (y):
    y = list(y)
    n = len(y)
    b = ''
    for i in range(0, n-1):
        aux = y[i]
        ran = random.randint(0, n-1)
        # ran = 4
        y[i] = y[ran]
        y[ran] = aux
    for i in y:
        b += i
    return(b)
        
y = input('Insira uma palavra: ')
print(embaralha(y))
# r = ['p', 'y', 't', 'h', 'o', 'n']
# ''.join(r) === r é uma lista qualquer
# Resultado === 'python'

# def join (n):
#     texto = ''
#     for i in texto: 
#         texto = '%s%s' % (texto, i)
#     return(texto)
        # FORMA EFICIENTE DE JUNTAR STRINGS/ELEMENTOS DE UMA LISTA