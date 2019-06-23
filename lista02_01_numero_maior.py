#Faca um programa que peca dois numeros e imprima o maior deles.

# != : diferente
# == : igual

a = float(input('Digite um numero: '))
b = float(input('Digite outro numero: '))

if a > b: 
    print('O numero %.2f eh maior que o numero %.2f ' % (a, b) )

elif b > a:
    print('O numero %.2f eh maior que o numero %.2f ' % (b, a))  

elif b == a:
    print('Os valores sao iguais')      

else: 
    print ('Valores invalidos')    



