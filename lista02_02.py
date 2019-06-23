#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.


a = float(input('Informe um numero qualquer: '))

if a > 0:
    print('O numero %.2f eh positivo' % (a))

elif a < 0: 
    print('O numero %.2f eh negativo' % (a)) 

else:
    print('O numero %.1f eh igual a zero' % (a)) 

