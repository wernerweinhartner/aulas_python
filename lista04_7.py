#Altere o programa anterior permitindo ao usuário informar as populações e as taxas 
# de crescimento iniciais. Valide a entrada e permita repetir a operação.


populacaoA = 0
populacaoB = 0

# crescA = float(input('Informe o crescimento da cidade A, em porcento: '))
# crescB = float(input('Informe o crewcimento da cidade B, em porcento: '))

# crescA = crescA/100
# crescB = crescB/100

# populacaoA = (populacaoA*crescA) + populacaoA
# populacaoB = (populacaoB*crescB) + populacaoB
# anos = 0

while populacaoA <= 0:
    populacaoA = input('Informe um valor válido para a cidade A: ')
    try:
        populacaoA = int(populacaoA)
    except:
        populacaoA = 0



while populacaoB <= 0:
    populacaoB = input('Informe um valor válido para a cidade B: ')
    try:
        populacaoB = int(populacaoB)
    except:
        populacaoB = 0


crescA = 0
crescB = 0

while crescA <= 0:
    try: 
        crescA = float(input('Informe o crescimento da cidade A, em porcento: '))
    except:
        crescA = 0

while crescB <= 0:
    try: 
        crescB = float(input('Informe o crewcimento da cidade B, em porcento: '))
    except: 
        crescB = 0

crescA = crescA/100
crescB = crescB/100

populacaoA = (populacaoA*crescA) + populacaoA
populacaoB = (populacaoB*crescB) + populacaoB
anos = 0

while populacaoA <= populacaoB: 
    anos += 1
    populacaoA = (populacaoA*crescA) + populacaoA
    populacaoB = (populacaoB*crescB) + populacaoB

# print(anos)
# print(populacaoA)
# print(populacaoB)

print('Em %d anos a população da cidade A ultrapassará a da cidade B'%(anos))
print('Quando isso ocorrer, a população da cidade A será de %d habitantes e a da cidade B será de %d habitantes'%(populacaoA, populacaoB))