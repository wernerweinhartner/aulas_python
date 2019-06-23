#Faça um Programa que solicite o sexo da pessoa, 
# verifique se a letra digitada é "F" ou "M" (maiúsculos ou minúsculos).
#  Conforme a letra escrever: F = Feminino, M = Masculino,
#  qualquer outro valor informado deve exibir "Sexo Inválido".


a = input('Informe seu sexo - M para masculino e F para feminino: ')
# a = a.upper() upper converte para letra maiuscula



if a == 'M' or a == 'm':
    print('Você pertence ao sexo masculino.')

elif a == 'F' or a == 'f':
    print('Você pertence ao sexo feminino.')

else:
    print('Sexo inválido.')


#upper, lower, replace

#len = mostra o tamanho de algo
#count  = mostra quantas vezes algo aparece

