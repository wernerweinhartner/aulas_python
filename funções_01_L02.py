#Faça um programa para imprimir: 
# 	1
# 	1   2
# 	1   2   3
# 	.....
# 	1   2   3   ...  n
# Para um n informado pelo usuário. 
# Use uma função que receba um valor n inteiro imprima até a n-ésima linha. 


n = int(input('Insira um numero: '))
def pascal(n):
    b = 0
    lista1 = []
    lista2 = []
    for i in range(1, n+1):
        if i < n:
            lista1.append(i)
            lista2 = str(lista1).strip('[]')
            print(lista2)
        elif i == n:
            lista1.append(i)
            # a função STRIP funciona com strings e tira dela um elemento específico
            lista2 = str(lista1).strip('[]')
        
    return(lista2)

print(pascal(n))

"""
função

"""
#Outra forma de fazer comentários. Geralmente com várias linhas de texto