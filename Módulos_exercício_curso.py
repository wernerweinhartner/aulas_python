#1 palavra 5  vezes seguidas, mostrar o tempo em um gráfico
import time
import matplotlib.pyplot as plt  
def tempo():
    a = 0
    lista2 = []
    lista = []
    legenda = []
    cont = 0
    again = int(input('Informe quantas vezes gostaria de repetir uma palavra: '))
    while a < again:
        inicio = time.clock()
        palavra = input('Insira uma palavra %d vezes: ' % (again))
        fim = time.clock()
        cont = fim - inicio
        lista.append(cont)
        a += 1
        word = str(a) +'a vez'
        legenda.append(word)
        lista2.append(a)
    print('Obrigado por usar o programa')
    x = lista2
    y = lista
    plt.xticks(x, legenda)
    plt.plot(x, y)
    plt.show()
    
tempo()


