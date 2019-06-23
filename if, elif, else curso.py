#if, elif e else: condicionais

idade = int(input('Digite a sua idade: '))
sexo = input('Digite o sexo M ou F: ').lower()

#if idade < 18 and sexo == 'm':
    #print('Homem menor de idade')

#elif idade >= 18 and sexo == 'm':
    #print('Homem maior de idade')

#elif idade < 18 and sexo == 'f':
    #print('Mulher menor de idade')

#elif idade >= 18 and sexo == 'f':
    #print('Mulher menor de idade')

#else:
    #print('Erro')





if sexo == 'm':
    if idade < 18:
        print('Homem menor de idade')
    else: 
        print('Homem maior de idade')

elif sexo == 'f':
    if idade < 18:
        print('Mulher menor de idade')
    else:
        print('Mulher maior de idade')

else: 
    print('Erro')    









