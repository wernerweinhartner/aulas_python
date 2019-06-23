# Faça um programa que leia 5 números e informe a soma e a média dos números.

lista = []

for i in range(0,5):
    lista.append(float(input('Informe um numero: ')))

media = 0
for item in lista:
    media += item

print(media)

media2 = media/len(lista)
print(media2)