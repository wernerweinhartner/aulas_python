#Faça um Programa que receba 
# uma quantidade pré determinada de notas e mostre as notas e a média na tela


# a = False
# while a == False:
#     qtd = input('Informe quantas notas você gostaria de analisar: ')
#     try: 
#         qtd = int(qtd)
#         if qtd > 0:
#             a == True
#             break
#         else: 
#             a = False
#     except:
#         a = False

#None === valor vazio

qtd = 0
while qtd <= 0:
    try:
        qtd = int(input('Informe quantas notas você gostaria de analisar: '))
    except:
        qtd = 0

#print(qtd)

a = 0
nota = 0
nota2 = []

while a < qtd:
    try:
        nota = float(input('Insira a nota: '))
        # nota = float(nota)
        if nota >= 0:
            nota2.append(nota)
            a += 1
        # else:
        #     nota = 0
    except: 
        # nota = 0
        pass

print(nota2)
soma = 0
for i in nota2:
    soma += i

media = soma/qtd

for i in nota2:
    print('Nota: %.2f' % (i))
    
print('Média das notas: %.2f ' % (media))

# import math
# print(math.pi)




