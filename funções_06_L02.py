#Faça uma função que 
# informe a quantidade de dígitos de um determinado número inteiro informado.
n = False
while n == False:
    n = input('Insira um número inteiro: ')
    try:
        n = int(n)
        if n > 0:
            n == True
        else: 
            print('Inválido')
            n = False
    except:
        print('Inválido')
        n = False

def digitos(n):
    a = 0
    n = str(n)
    n = list(n)
    for i in n:
        a += 1
    return(a)

print('O número inserido tem %d dígitos' % (digitos(n)))

#PODERIA TER USADO LEN(STRING)