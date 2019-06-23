#Faça um programa que leia 5 números e informe a soma e a média dos números.


lista = []
#tamanho = 5
i = 1

while i != 0:
    #i += 1
    #lista.append(int(input('Informe um número: ')))
    i = int(input('Informe um número: '))
    if i != 0:
        lista.append(i)


# soma = lista[0] + lista[1] + lista[2] + lista[3] + lista[4]
# print(soma)

# media = soma/tamanho

# print(media)


soma = 0
for i in lista:
    soma += i

print(soma)
media = soma/len(lista)
print(media)   


