#Faça um programa, com uma função que necessite de três argumentos, 
# e que forneça a soma desses três argumentos.

# a = float(input('Insira um numero: '))
# b = float(input('Insira um numero: '))
# c = float(input('Insira um número: '))

n = False
while n == False:
    n = input('Quantos números gostaria de somar? ')
    try:
        n = int(n)
        if n > 0:
            n == True
        else:
            print('Número inválido')
            n = False
    except:
        print('Número inválido')
        n = False

def soma(n):
    lista = []
    a = 0
    while a < n:
        numeros = float(input('Insira um numero: '))
        lista.append(numeros)
        a += 1
    soma = sum(lista)
        # função SUM soma os elementos de uma lista
    return(soma)     
        
print(soma(n))


# a = float(input('Insira um número: '))
# b = float(input('Insira um número: '))
# c = float(input('Insira um número: '))
# def soma(a ,b, c):
#     soma = a + b + c
#     return soma

# print(soma(a, b, c))


