#Faça um Programa que leia três números e mostre o maior deles.

a = float(input('Digite um número: '))
b = float(input('Digite um número: '))
c = float(input('Digite um número: '))
maior = None

if a > b and a > c:
    maior = a
elif b > a and b > c: 
    maior = b
elif c > a and c > b:
    maior = c

print('O maior numero eh: %d' % (maior))    

#none = falso, vazio    


    
            