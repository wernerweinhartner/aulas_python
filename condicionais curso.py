#exercicio de condicionais

nome = input('Digite o nome do aluno: ')
nota1 = float(input('Digite a nota da primeira prova: '))
nota2 = float(input('Digite a nota da segunda prova: '))
faltas = int(input('Digite o total de faltas do aluno: '))

percentual_de_presença = str(100 - ((faltas/20)*100))
media = (nota1 + nota2)/2

if faltas <= 7 and media >= 6:
    print('Nome do aluno: %s' % (nome))
    print('Média: %.2f' % (media))
    print('Percentual de presença (assiduidade): %s' % (percentual_de_presença)+'%')
    print('Resultado: Aprovado')

elif faltas >= 7 and media >= 6:
    print('Nome do aluno: %s' % (nome))
    print('Média: %.2f' % (media))
    print('Percentual de presença (assiduidade): %s' % (percentual_de_presença)+'%')
    print('Resultado: Reprovado por faltas')

elif faltas <= 7 and media <=6:
    print('Nome do aluno: %s' % (nome))
    print('Média: %.2f' % (media))
    print('Percentual de presença (assiduidade): %s' % (percentual_de_presença)+'%')
    print('Resultado: Reprovado por média')    

elif faltas >= 7 and media <=6:
    print('Nome do aluno: %s' % (nome))
    print('Média: %.2f' % (media))
    print('Percentual de presença (assiduidade): %s' % (percentual_de_presença)+'%')
    print('Resultado: Reprovado por faltas e média')    

else:
    print('Erro')
  

