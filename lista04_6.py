#Supondo que a população de um país A seja da ordem de 80000 habitantes com
#  uma taxa anual de crescimento de 3% e 
# que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
#  Faça um programa que calcule e escreva o número de anos necessários para que 
# a população do país A ultrapasse ou iguale a população do país B,
#  mantidas as taxas de crescimento

populacaoA = 80000
populacaoB = 200000

crescA = 0.03
crescB = 0.015


anos = 0
while populacaoA < populacaoB: 
    anos += 1
    populacaoA = (populacaoA*crescA) + populacaoA
    populacaoB = (populacaoB*crescB) + populacaoB

# print(anos)
# print(populacaoA)
# print(populacaoB)

print('Em %d anos a população do país A ultrapassará a do país B'%(anos))
print('Quando isso ocorrer, a população do país A será de %d habitantes e a do país B será de %d habitantes'%(populacaoA, populacaoB))


# popA = 80000
# popB = 200000

# ano = 0
# while(popA < popB):
#     ano += 1
#     popA = popA * 1.03
#     popB = popB * 1.015
#     print("população A: %f" % (popA))
#     print("população B: %f" % (popB))
#     print('')

# print("Total de anos: %d " % ano)



