

peso1 = 0
peso2 = 0

while peso1 == 0 or peso2 == 0: 
    peso1 = float(input('Insira o peso da primeira prova: '))
    peso2 = float(input('Insira o peso da segunda prova:  '))

nota1 = 0
nota2 = 0

while nota1 == 0 or nota2 == 0:
    nota1 = float(input('Insira a nota da primeira prova: '))
    nota2 = float(input('Insira a nota da segunda prova: '))

media = float(((nota1*peso1) + (nota2*peso2))/(peso1+peso2))
print('A sua media é: ', media)
