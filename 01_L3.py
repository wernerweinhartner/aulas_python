#Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e 
# continue pedindo até que o usuário informe um valor válido.
#max(lista): mostra o maior valor dentro de uma lista/array
#list converte em lista
# ctrl + / = comenta algo 
# ctrl + a  = seleciona tudo

# a = float(input('Informe uma nota de zero a dez: '))

# while a < 0.0 or a > 10.0: 
#     print('Valor inválido')
#     a = float(input('Informe uma nota de zero a dez: '))

# if 0.0 <= a <= 10.0: 
#     print('Nota válida')    
 
        
#o comando break força o while a parar 

nota = ''

while not nota.isdigit(): 
    nota = input('Informe uma nota entre 0 e 10: ')
    if nota.isdigit():
        nota = float(nota)
        if nota < 0.0 or nota > 10.0:
            nota = ''
        else: 
            break

print('Você digitou %s' % (nota))            

    








