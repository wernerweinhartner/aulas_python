#Faça um Programa que peça as 4 notas bimestrais e mostre a média.


a = input('A primeira nota bimestral é: ')
b = input('A segunda nota bimestral é: ')
c = input('A terceira nota bimestral é:')
d = input('A quarta nota bimestral é: ')

media = (float(a) + float(b) + float(c) + float(d)) / 4.0

print('A media das notas bimestrais é: %.1f' % (media))

