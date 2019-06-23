#Faça um programa, com uma função que necessite de um argumento. 
# A função retorna o valor de caractere ‘P’, 
# se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.




a = 0
b = False
while b == False:
    a = input('Insira um número: ')
    try:
        a = float(a)
        b = True
    except:
        print('Número inválido')
        b = False

def sinal(a):
    sinal = ''
    if a > 0:
        sinal = 'P'
        print('O número inserido é positivo')
    elif a <= 0:
        sinal = 'N'
        print('O número inserido é negativo ou igual a zero')
    return(sinal)

print(sinal(a))
    
