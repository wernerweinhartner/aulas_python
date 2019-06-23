#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

a = input('Digite uma letra: ')

if a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u':
    print('Essa letra é uma vogal.')

elif not a.isdigit():
    print('Essa letra é uma consoante.')
    
else: 
    print('Eh um numero.')    