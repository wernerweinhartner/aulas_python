#ler um numero inteiro e mostar invertido
#para reverter uma string === a = a[::-1]
#para reverter uma lista === lista.reverse()

numero = []

a = 0
y = 0
x = int(input('Quantos numeros deseja inserir?: '))

if x == 1:
    a = input('Insira um número: ')
    print(a)
    a = a[::-1]
    print(a)
else:
    while y < x:
        y += 1
        a = int(input('Insira um número: '))
        numero.append(a)

    print(numero)
    numero.reverse()

    print(numero)