#Desenha moldura.
#  Construa uma função que desenhe um retângulo usando os caracteres
#  ‘+’ , ‘−’ e ‘| ‘. 
# Esta função deve receber dois parâmetros, linhas e colunas, 
# sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20.
#  Se valores fora da faixa forem informados,
#  eles devem ser modificados para valores dentro da faixa de forma elegante.
a = False
while a == False:
    a = input('Insira o número de linhas: ')
    try:
        a = int(a)
        if 0 < a <= 20:
            a == True
        else:
            print('Inválido')
            a = False
    except:
        print('Inválido')
        a = False

b = False
while b == False:
    b = input('Insira o número de colunas: ')
    try: 
        b = int(b)
        if 0 < b <= 20:
            b == True
        else:
            print('Inválido')
            b = False
    except:
        print('Inválido')
        b = False

colunas = ''
moldura = ''
linhas = ''
def ret(colunas, linhas):
    colunas = ' ' + b*'-' + ' '
    inicio = '+' + colunas + '+'
    print(inicio)
    moldura = '|' + colunas + '|'
    for i in range(0, a-2):
        print(moldura)
    linhas = a*(colunas) + a*(moldura)
    # for i in range(0, a-1):
    #     print(linhas)
    fim = '+' + colunas + '+'
    if b >= 1 and a > 1:
        print(fim)
    return(colunas, linhas)

ret(colunas, linhas)