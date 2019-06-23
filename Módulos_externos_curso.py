#Módulos externos do python:
#É preciso download o arquivo (geralmente)
# pip install (nome do arquivo) === para baixar
# Módulos importantes:
# Scipy/matplotlib
# sql alchemy
# pygame
# wxpython

import matplotlib.pyplot as plt  
x = [1, 2, 3, 4, 5, 6] #grafico so pode ter numeros
y = [1500, 1800, 1300, 1900, 2100, 2000] 
# plt.plot(x, y)
# plt.show() #imprimir o gráfico 
legenda = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']
plt.xticks(x, legenda) #substitui uma lista por outra, pode ter string
plt.plot(x, y)
plt.show()
