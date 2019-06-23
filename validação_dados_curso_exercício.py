#exercicio de validação de dados
#media tem que ser maior que 6
#ao menos 70% de presença

nota1 = False
nota2 = False
presença = False
media = 0

while nota1 == False:
    nota1 = input('Insira a nota da primeira prova: ')
    try: 
        nota1 = float(nota1)
        while nota1 <= 0 or nota1 > 10:
            nota1 = float(input('Insira um valor de 0 a 10: '))
        nota1 == True
        break
    except: 
        print('Insira um valor válido')
        nota1 = False


#print(nota1)

while nota2 == False:
    nota2 = input('Insira a nota da segunda prova: ')
    try: 
        nota2 = float(nota2)
        while nota2 <= 0 or nota2 > 10:
            nota2 = float(input('Insira um valor de 0 a 10: '))
        nota2 == True
        break
    except: 
        print('Insira um valor válido')
        nota2 = False

#print(nota2)

media = (nota1 + nota2)/2.0


while presença == False:
    presença = input('Insira o número de aulas comparecidas pelo aluno: ')
    try:
        presença = float(presença)
        while presença <= 0 or presença >= 20:
            presença = input('Insira um valor válido de 0 a 20: ')
        presença == True
        break

    except: 
        print('Insira um valor válido')
        presença = False
        continue


#print(presença)
faltas = 20 - presença


if media >= 6: 
    print('Sua nota é: %.2f' % (media))
    print('Número de faltas: %d' % (faltas))
    if presença >= 14:
        print('Aprovado')
    elif presença < 14:
        print('Reprovado por falta')

elif media < 6:
    print('Sua nota é: %.2f' % (media))
    print('Número de faltas: %d' % (faltas))
    if presença >= 14:
        print('Reprovado por média')

    elif presença < 14:
        print('Reprovado por média e presença')            

