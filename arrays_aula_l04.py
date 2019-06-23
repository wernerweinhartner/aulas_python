#Faça um Programa que leia um vetor de 5 números inteiros positivos e mostre-os.


lista = []

while len(lista) < 5: 
    try:
        numero = int(input('Insira um número inteiro positivo: '))
        if numero >= 0:
            lista.append(numero)
    except:
        pass
    #lista.append(numero)

print(lista)
# lista2 = []

# for i in lista:
#     lista2.append(i)

# lista2.reverse()

# print(lista2)
#SUNSTITUINDO A FUNÇÃO REVERSE (MANUAL)
aux = []

while len(lista) > 0:
    aux.append(lista.pop())

print(aux)

#POP === remove o ultimo elemento de uma lista

