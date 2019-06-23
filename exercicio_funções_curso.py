#IMC
#Sexo
#Altura
#Classificação

sexo = ''
def imc(peso, altura):
    imc = (peso/(altura**2))
    #print(imc)
    return(imc)



while sexo == '':
    sexo = input("Insira seu sexo, 'm' para mulher e 'h' para homem: ").lower()
    if sexo == 'm':
        sexo = 'Mulher'
    elif sexo == 'h':
        sexo = 'Homem'    
    elif sexo != 'm' and sexo != 'h':
        print('Sexo inválido')
        sexo = ''

#print(sexo)

peso = False

while peso == False:
    peso = input('Insira seu peso, em kilogramas: ')
    try:
        peso = float(peso)
        if peso > 0:
            peso == True
            break
        else:
            print('Peso inválido')
            peso = False
    except: 
        print('Peso inválido')   
        peso = False


#print(sexo, peso)

altura = False

while altura == False:
    altura = input('Insira sua altura, em metros: ')
    try:
        altura = float(altura)
        if altura > 0:
            altura == True
            break
        else: 
            print('Altura inválida')
            altura = False
    except: 
        print('Insira uma altura válida: ')
        altura = False

#print(sexo, peso, altura)
imc2 = ''

if sexo == 'Mulher':
    imc(peso, altura)
    if imc(peso, altura) <= 19.1:
        imc2 = 'Abaixo do peso'
    elif 19.1 < imc(peso, altura) <= 25.8:
        imc2 = 'Peso normal'
    elif 25.8 < imc(peso, altura) <= 27.3:
        imc2 = 'Marginalmente acima do peso'
    elif 27.3 < imc(peso, altura) <= 32.3:
        imc2 = 'Acima do peso ideal'
    elif imc(peso, altura) > 32.3:
        imc2 = 'Obeso'
if sexo == 'Homem':
    imc(peso, altura)
    if imc(peso, altura) <= 20.7:
        imc2 = 'Abaixo do peso'
    elif 20.7 < imc(peso, altura) <= 26.4:
        imc2 = 'Peso normal'
    elif 26.4 < imc(peso, altura) <= 27.8:
        imc2 = 'Marginalmente acima do peso'
    elif 27.8 < imc(peso, altura) <= 31.1:
        imc2 = 'Acima do peso ideal'
    elif imc(peso, altura) > 31.1:
        imc2 = 'Obeso' 

print('O seu sexo é: %s' % (sexo))
print('O seu peso é: %.2f kg' % (peso))
print('A sua altura é: %.1f m' % (altura))   
print('O seu IMC é: %.2f' % (imc(peso, altura)))
print('A sua condição é: %s' % (imc2))



