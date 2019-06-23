#Faça um programa que converta da notação de 24 horas para a notação de 12 horas. 
# Por exemplo, o programa deve converter 14:25 em 2:25 P.M. 
# A entrada é dada em dois inteiros. 
# Deve haver pelo menos duas funções: 
# uma para fazer a conversão e uma para a saída.
#  Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. 
# Assim, a função para efetuar as conversões terá um parâmetro formal 
# para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário 
# repita esse cálculo para novos valores de entrada todas as vezes que desejar.

#hora = input('Insira um horário no formato 24 horas: ')
hora = ''
#print(hora)

def horario(hora):
    novo = ''
    #horas, minutos = hora.split(':')
    horas = False
    while horas == False:
        hora = input('Insira um horário no formato 24 horas: ')
        try:
            horas, minutos = hora.split(':')
            minutos = int(minutos)
            horas = int(horas)
        except: 
            print('Inválido')
            horas = False
        try:
            horas = int(horas)
            minutos = int(minutos)
            if horas < 0 or minutos < 0:
                print('Inválido')
                horas = False
            elif horas > 24 or minutos > 59:
                print('Inválido')
                horas = False
            elif 0 <= horas <= 24 and 0 <= minutos <= 59:
                horas == True
                # horas = int(horas)
                # minutos = int(minutos)
                #horas, minutos = hora.split(':')
        except:
            print('Inválido')
            horas = False
    tipo = ''
    if 12 < horas <= 24:
        pm = 24 - horas
        am = 0
        if pm == 0:
            am = 0
            tipo = 'AM'
        elif pm != 0:
            #tipo = 'PM'
            am = 12 - pm
            tipo = 'PM'
        # if pm == 0:
        #     tipo = 'AM'
        # elif pm != 0:
        #     tipo = 'PM'
    elif 0 < horas < 12:
        pm = horas
        am = pm
        tipo = 'AM'
    elif horas == 12:
        pm = horas
        am = pm
        tipo = 'PM' 
    if 0 <= minutos < 10:
        minutos = str('0' + str(minutos))
    novo = str(am) + ':' + str(minutos) + tipo 
    # print(novo)
    return('Horário no formato 12 horas: %s' % (novo))
#teste: %0.3d(para inteiros) % 2
#isso vai retornar algo com 3 digitos
# teste: 002
print(horario(hora))

pergunta = input('Gostaria de repetir a operação (sim ou não)? ')
if pergunta == 'não':
        print('Obrigado por usar o programa')
while pergunta == 'sim':
    hora = ''


    def horario(hora):
        novo = ''
        #horas, minutos = hora.split(':')
        horas = False
        while horas == False:
            hora = input('Insira um horário no formato 24 horas: ')
            try:
                horas, minutos = hora.split(':')
                #função split quebra uma string em um determinado ponto
                #antes disso, deve haver as variaveis nas quais as informações 
                #vão ser armazenadas. Ver exemplo acima
                minutos = int(minutos)
                horas = int(horas)
            except: 
                print('Inválido')
                horas = False
            try:
                horas = int(horas)
                minutos = int(minutos)
                if horas < 0 or minutos < 0:
                    print('Inválido')
                    horas = False
                elif horas > 24 or minutos > 59:
                    print('Inválido')
                    horas = False
                elif 0 <= horas <= 24 and 0 <= minutos <= 59:
                    horas == True
                    # horas = int(horas)
                    # minutos = int(minutos)
                    #horas, minutos = hora.split(':')
            except:
                print('Inválido')
                horas = False
        tipo = ''
        if 12 < horas <= 24:
            pm = 24 - horas
            am = 0
            if pm == 0:
                am = 0
                tipo = 'AM'
            elif pm != 0:
                #tipo = 'PM'
                am = 12 - pm
                tipo = 'PM'
            # if pm == 0:
            #     tipo = 'AM'
            # elif pm != 0:
            #     tipo = 'PM'
        elif 0 < horas < 12:
            pm = horas
            am = pm
            tipo = 'AM'
        elif horas == 12:
            pm = horas
            am = pm
            tipo = 'PM' 
        if 0 <= minutos < 10:
            minutos = str('0' + str(minutos))
        novo = str(am) + ':' + str(minutos) + tipo 
        # print(novo)
        return('Horário no formato 12 horas: %s' % (novo))

    print(horario(hora))
    pergunta = input('Gostaria de repetir a operação (sim ou não)? ')
    