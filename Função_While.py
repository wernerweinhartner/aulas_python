letra = ''
contador = 0
while(letra != 'a'):
    #contador = contador + 1
    contador += 1
    print('Repeticao N: %d' % (contador))
    letra = input("Informe a letra 'a': ")
    if letra == 'a':
        print('Parabéns!')

