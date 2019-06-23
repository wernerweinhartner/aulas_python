# módulos built-in parte 1:
# built-in são aquelas já criadas e estão no python

# import math

# math.ceil # === faz arrendondamento para cima
# math.floor # === faz arredondamento para baixo 
# math.fsum() # === faz a soma de elementos de uma lista. É um somatório
# math.sqrt() # === faz a raiz quadrada de um número

# import time
# time.localtime() # === armazena o horario, dia da semana etc 
# hora = time.localtime().tm_hour # === armazena a hora especificamente
# time.clock()
import time
def cont_tempo():
    inicio = time.clock()
    input('Escreva seu nome: ')
    fim = time.clock()
    tempo = round(fim - inicio, 3)
    print('Você levou %s segundos para escrever o seu nome' % (tempo))

cont_tempo() 

# a função ROUND arredonda números, com x casas decimais