# Faça um programa que leia 5 números e informe o maior número

lista = []

for i in range(0,5):
    lista.append(int(input('Informe um valor: ')))

print(max(lista))

