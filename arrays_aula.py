# -*- encoding: utf-8 -*-
#arrays 
#list
#
# lista = [1,'2',['item1', 'item2']]


# print(lista[2][0])


#Faça um programa que leia 5 números e informe o maior número
# variavel += variavel ==== incrementa a variavel + a variavel
#while tem que ter uma variavel de controle
#variavel[0:posição final] ===== recorta a variavel


lista = []
tamanho = 5
i = 0
while i < tamanho:
    i += 1
    lista.append(int(input('Informe um número: ')))




resultado = ''
for i in lista:
    resultado += '%s, ' %(i)
    
resultado = resultado[0:len(resultado)-2]

print('Resultado: %s' % (resultado))   
print(max(lista))     
    



    




