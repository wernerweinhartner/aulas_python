#Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
#Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
# Imprima os três vetores. 
# OBS: para saber se um número é par ou ímpar use o operador mod, 
# ele resulta no resto da divisão, ex:
# (10 % 2) resulta em 0, pois o resto da divisão de 10 por 2 é 0;
# (11 % 2) resulta em 1, pois o resto da divisão de 10 por 2 é 1;
# Então, sempre que o resultado de X % 2 for igual a zero, X é par.
# % = mod === mostra o resto da divisão

a = 0

b = False
while b == False:
    b = input('Informe quantos números você deseja que sejam analisados: ')
    try:
        b = int(b)
        break
    except:
        print('Insira um valor válido')
        b = False

num = 0
lista = []
while a < b:
    num = input('Insira um número (%d vezes): ' % (b))
    try:
        num = int(num)
        lista.append(num)
        a += 1 
    except:
        print('Insira um valor válido')
        continue

print('Lista de números: ', lista)


pares = []
impares = []

for i in lista:
    resultado = i % 2
    if resultado == 0:
        pares.append(i)
    else:
        impares.append(i)

pares = str(pares)
impares = str(impares)
print('Números pares: %s' % (pares))
print('Números ímpares: %s' % (impares))