#primeiro capturar os dados necessários.
#depois fazer os devidos testes.
#se colocar dois if, duas situações serao consideradas
#if(começa ciclos) + elif(quantos quiser) + else
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

sexo = input('Digite m para mulher ou h para homem: ')
altura = float(input('Digite sua altura: '))

if sexo == 'm' or sexo == 'M':
    peso_ideal = ((62.1 * altura) - 44.7)
    print('Seu peso ideal eh: %.3f' % (peso_ideal))


elif sexo == 'h' or sexo == 'H':
    peso_ideal = ((72.7*altura) - 58)
    print('Seu peso ideal eh: %.3f ' % (peso_ideal))

else:
    print('Valor invalido')

print('fim')

#Crtl + s = salvar
#função AND: adiciona coisas, condições
#booleano: verdadeiro ou falso
# Ex: 1 == 2  false
















